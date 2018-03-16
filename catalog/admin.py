from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from django import forms

from .models import Concept
from .models import TaskInConcept
from .models import Tag
from .models import Task
from .models import Grade
from .models import Student
from .models import TaskText
from .models import TaskSessionGroup
from .models import Session


def translate(name):
    # Заменяем пробелы и преобразуем строку к нижнему регистру
    name = name.replace(' ', '_').lower()
    name = name.replace('.', '').lower()
    name = name.replace(',', '').lower()
    name = name.replace('/', '').lower()
    name = name.replace('(', '').lower()
    name = name.replace(')', '').lower()
    name = name.replace('%', '').lower()
    name = name.replace('&', '').lower()
    name = name.replace('$', '').lower()
    name = name.replace('"', '').lower()
    name = name.replace("'", '').lower()
    name = name.replace("!", '').lower()
    name = name.replace("#", '').lower()
    name = name.replace("^", '').lower()
    name = name.replace("*", '').lower()
    name = name.replace("+", 'plus').lower()
    name = name.replace(":", '').lower()
    name = name.replace(";", '').lower()
    name = name.replace("№", '').lower()
    name = name.replace('-', 'minus').lower()
    name = name.replace('>', '_').lower()
    name = name.replace('<', '_').lower()
    name = name.replace('?', '_').lower()
    name = name.replace('=', 'ravno').lower()
    name = name.replace('|', '_').lower()

    #
    transtable = (
        ## Большие буквы
        (u"Щ", u"Sch"),
        (u"Щ", u"SCH"),
        # two-symbol
        (u"Ё", u"Yo"),
        (u"Ё", u"YO"),
        (u"Ж", u"Zh"),
        (u"Ж", u"ZH"),
        (u"Ц", u"Ts"),
        (u"Ц", u"TS"),
        (u"Ч", u"Ch"),
        (u"Ч", u"CH"),
        (u"Ш", u"Sh"),
        (u"Ш", u"SH"),
        (u"Ы", u"Yi"),
        (u"Ы", u"YI"),
        (u"Ю", u"Yu"),
        (u"Ю", u"YU"),
        (u"Я", u"Ya"),
        (u"Я", u"YA"),
        # one-symbol
        (u"А", u"A"),
        (u"Б", u"B"),
        (u"В", u"V"),
        (u"Г", u"G"),
        (u"Д", u"D"),
        (u"Е", u"E"),
        (u"З", u"Z"),
        (u"И", u"I"),
        (u"Й", u"J"),
        (u"К", u"K"),
        (u"Л", u"L"),
        (u"М", u"M"),
        (u"Н", u"N"),
        (u"О", u"O"),
        (u"П", u"P"),
        (u"Р", u"R"),
        (u"С", u"S"),
        (u"Т", u"T"),
        (u"У", u"U"),
        (u"Ф", u"F"),
        (u"Х", u"H"),
        (u"Э", u"E"),
        (u"Ъ", u"`"),
        (u"Ь", u"'"),
        ## Маленькие буквы
        # three-symbols
        (u"щ", u"sch"),
        # two-symbols
        (u"ё", u"yo"),
        (u"ж", u"zh"),
        (u"ц", u"ts"),
        (u"ч", u"ch"),
        (u"ш", u"sh"),
        (u"ы", u"yi"),
        (u"ю", u"yu"),
        (u"я", u"ya"),
        # one-symbol
        (u"а", u"a"),
        (u"б", u"b"),
        (u"в", u"v"),
        (u"г", u"g"),
        (u"д", u"d"),
        (u"е", u"e"),
        (u"з", u"z"),
        (u"и", u"i"),
        (u"й", u"j"),
        (u"к", u"k"),
        (u"л", u"l"),
        (u"м", u"m"),
        (u"н", u"n"),
        (u"о", u"o"),
        (u"п", u"p"),
        (u"р", u"r"),
        (u"с", u"s"),
        (u"т", u"t"),
        (u"у", u"u"),
        (u"ф", u"f"),
        (u"х", u"h"),
        (u"э", u"e"),
        (u"ь", u""),
    )
    # перебираем символы в таблице и заменяем
    for symb_in, symb_out in transtable:
        name = name.replace(symb_in, symb_out)
    # возвращаем переменную
    return name


class IsTaskInAnyConceptFilter(admin.SimpleListFilter):
    title = ('is in any concept')
    parameter_name = 'isinanyconcept'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'да'),
            ('no', 'нет'),
        )

    def queryset(self, request, queryset):
        rids = [x.task.id for x in TaskInConcept.objects.all()]
        if self.value() == 'yes':
            return queryset.filter(id__in=rids)
        else:
            return queryset.exclude(id__in=rids)


admin.site.register(Tag)

class AddToConceptActionForm(ActionForm):
    concept_id = forms.IntegerField()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    action_form = AddToConceptActionForm

    fields = ('tlt', 'tags', 'example')
    filter_horizontal = ('tags',)
    list_display = ('id', 'code', 'tlt', 'example', 'is_in_any_concept', )
    list_filter = ('tags', IsTaskInAnyConceptFilter)
    ordering = ('id',)
    actions = ('add_to_concept', )

    def add_to_concept(self, request, queryset):
        c_id = request.POST['concept_id']
        c_id = int(c_id)
        for t in queryset:
            c = Concept.objects.get(id=c_id)

            qs = TaskInConcept.objects.filter(concept=c)
            if not qs.exists():
                o = 1
            else:
                o = max([x.order for x in qs]) + 1

            tic = TaskInConcept(concept=c, task=t, order=o)
            tic.save()

    add_to_concept.short_description = "Add to concept"

    def is_in_any_concept(self, obj):
        return Concept.objects.filter(tasks__id__contains=obj.id).exists()

    def save_model(self, request, obj, form, change):
        obj.code = translate(obj.tlt)
        super(TaskAdmin, self).save_model(request, obj, form, change)


class ConceptInGradeInline(admin.TabularInline):
    model = Grade.concepts.through
    ordering = ("order",)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
#    filter_horizontal = ('concepts'),
    fields = ('tlt', )
    list_display = ('tlt',)
    exclude = ('concepts', )
    inlines = [ConceptInGradeInline,]

    def save_model(self, request, obj, form, change):
        obj.code = translate(obj.tlt)
        super(GradeAdmin, self).save_model(request, obj, form, change)


class TaskInConceptInline(admin.TabularInline):
    model = Concept.tasks.through
    ordering = ("order",)

@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):

    fields = ('tlt', 'public')
    list_display = ('tlt', 'public')
    exclude = ('tasks', )
    inlines = [TaskInConceptInline,]

    def save_model(self, request, obj, form, change):
        obj.code = translate(obj.tlt)
        super(ConceptAdmin, self).save_model(request, obj, form, change)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskText)
class TaskTextAdmin(admin.ModelAdmin):
    ordering = ("order",)


class TaskSessionGroupInLine(admin.TabularInline):
    model = TaskSessionGroup
    extra = 0


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("student", "date")
    inlines = [TaskSessionGroupInLine,]

