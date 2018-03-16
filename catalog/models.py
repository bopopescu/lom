from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import gen.lib as l

def validate_unique_task_tlt(value):
    if value in [x.tlt for x in Task.objects.all()]:
        raise ValidationError(
            _('%(value)s is not uniqe'),
            params={'value': value},
        )

def validate_unique_concept_tlt(value):
    if value in [x.tlt for x in Concept.objects.all()]:
        raise ValidationError(
            _('%(value)s is not uniqe'),
            params={'value': value},
        )

class Grade(models.Model):
    code = models.CharField(max_length=200, unique=True)
    tlt = models.CharField(max_length=200)
    concepts = models.ManyToManyField('Concept', through='ConceptInGrade', blank=True)

    def __str__(self):
        return self.tlt


class Tag(models.Model):
    tlt = models.CharField(max_length=200)

    def __str__(self):
        return self.tlt


class Task(models.Model):
    default_version = 1

    code = models.CharField(max_length=200, unique=True)
    tlt = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    example = models.CharField(max_length=200, blank=True)
    ver = models.PositiveIntegerField(blank=False, default=default_version)

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.original_code = self.code
        self.original_tlt = self.tlt

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        method = getattr(l, self.original_code, "__none")
        if method != "__none":
            text, atext = method()
            self.example = text

        if self.original_tlt != self.tlt:
            t = Task.objects.all().order_by("-id")[0].pk
            test_code = self.code
            while Task.objects.filter(code=test_code).exists():
                t += 1
                test_code = self.code + str(t + 1)
            self.code = test_code
        else:
            self.code = self.original_code

        super(Task, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        ex = self.example
        ex = (ex[:100] + '..') if len(ex) > 100 else ex
        return self.tlt + " [" + ex + "]"

class Concept(models.Model):
    code = models.CharField(max_length=200, unique=True)
    tlt = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    tasks = models.ManyToManyField(Task, through='TaskInConcept', blank=True)

    def __str__(self):
        return self.tlt + ("(hidden)" if not self.public else "") + ", " + str(self.tasks.count())

class TaskInConcept(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(blank=True)


class ConceptInGrade(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(blank=True)


class Student(models.Model):
    login = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.login


class Session(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        if not self.student is None:
            return self.student.name + ": " + str(self.date)
        else:
            return "no user: " + str(self.date)


class TaskSessionGroup(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0)
    tlt_text = models.CharField(max_length=200)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.task != None:
            self.tlt_text = self.task.tlt
        super(TaskSessionGroup, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        if not self.session.student is None:
            res = self.session.student.name
        else:
            res = "no user"
        return res + " " + str(self.session.date) + " " + str(self.order) + ": " + self.tlt_text


class TaskText(models.Model):
    text = models.CharField(max_length=1000)
    atext = models.CharField(max_length=1000)
    order = models.PositiveIntegerField(default=0)
    group = models.ForeignKey(TaskSessionGroup, on_delete=models.CASCADE)

    def __str__(self):
        trimmed_text = (self.text[:100] + '..') if len(self.text) > 100 else self.text
        if not self.group.session.student is None:
            res = self.group.session.student.name
        else:
            res = "no user"
        return res + " " + str(self.group.session.date) + ": " + str(self.group.order) + " " + self.group.tlt_text + ": "\
               +  str(self.order) + " " + trimmed_text