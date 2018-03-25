from django.shortcuts import render
import gen.lib as l
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import datetime
import catalog.models as m

FROM_CODE = False


def filter_grades():
    filtered_grades = {}
    for g in l.grades.keys():
        filtered_concepts = []
        new_grade = l.grades[g]
        for c in l.grades[g]['concepts']:
            if l.concepts[c]['public']:
                filtered_concepts.append(c)
        if len(filtered_concepts) > 0:
            new_grade['concepts'] = filtered_concepts
            filtered_grades[g] = new_grade
    return filtered_grades


def updateParamsFromDatabase():
    if FROM_CODE:
        return

    l.grades = {}
    l.concepts = {}
    l.tasks = {}
    l.task_order_in_concept = {}

    for t in m.Task.objects.all():
        if getattr(l, t.code, "__none") != "__none":
            ex = t.example.replace("'", "")
            ex = (ex[:100] + '..') if len(ex) > 100 else ex
            l.tasks[t.code] = {'title': t.tlt, 'example': ex}
            l.tasks[t.code]['orders'] = {}

    for c in m.Concept.objects.all():
        tasks_array = []
        for t in c.tasks.all():
            if t.code in l.tasks:
                tic = m.TaskInConcept.objects.get(task=t, concept=c)
                order = tic.order
                tasks_array.append((t.code, order))

        def get_task_order(t1):
            t_code, t_order = t1
            return t_order

        tasks_array = sorted(tasks_array, key=get_task_order, reverse=False)

        if len(tasks_array) > 0:
            l.concepts[c.code] = {'public': c.public, 'title': c.tlt}
            l.concepts[c.code]['tasks'] = [t_code for t_code, t_order in tasks_array]

    for g in m.Grade.objects.all():
        l.grades[g.code] = {'title': g.tlt}
        concepts_array = []
        for c in g.concepts.all():
            if c.code in l.concepts:
                cig = m.ConceptInGrade.objects.get(grade=g, concept=c)
                concepts_array.append((c.code, cig.order))
        concepts_array.sort(key=lambda x: x[1])
        l.grades[g.code]['concepts'] = [x[0] for x in concepts_array]


def is_teacher(user):
    if user:
        return user.groups.filter(name='teachers').exists()
    else:
        return False

def get_session_data(session_id):
    objSession = m.Session.objects.get(pk=session_id)

    s = {}
    s['date'] = objSession.date
    if objSession.student:
        s['student_name'] = objSession.student.name
        s['student_login'] = objSession.student.login
    else:
        s['student_name'] = ""
        s['student_login'] = ""
    if objSession.note:
        s['note'] = objSession.note
    else:
        s['note'] = ""

    session_groups_list = []
    for tg in m.TaskSessionGroup.objects.all():
        session = m.Session.objects.get(pk=session_id)
        if tg.session == session:
            tg_dict = {}
            tg_dict['tlt'] = tg.tlt_text
            tg_dict['task_code'] = tg.task.code
            tg_dict['note'] = "" if not tg.note else tg.note

            texts_list = []
            for t in m.TaskText.objects.all():
                if t.group == tg:
                    texts_list.append((t.text, t.atext, t.note if t.note else "", t.order))

            texts_list.sort(key=lambda x: x[3])
            tg_dict['texts'] = [(x[0], x[1], x[2]) for x in texts_list]
            tg_dict['order'] = tg.order

            session_groups_list.append(tg_dict)

    session_groups_list.sort(key=lambda x: x['order'])
    for x in session_groups_list:
        x.pop('order', None)
    s['groups'] = session_groups_list
    return s

def date_converter(obj):
    if isinstance(obj, datetime.date):
        return obj.__str__()

@login_required(login_url='/login/')
@user_passes_test(is_teacher, login_url='/login/')
def index(request):
    updateParamsFromDatabase()

    filtered_grades = filter_grades()
    return render(request, 'catalog.html', context={
        'grades': json.dumps(filtered_grades),
        'concepts': json.dumps({c:l.concepts[c] for c in l.concepts.keys() if l.concepts[c]['public']}),
        'tasks': json.dumps(l.tasks),
    })

@login_required(login_url='/login/')
@user_passes_test(is_teacher, login_url='/login/')
def get_session(request, session_id):
    updateParamsFromDatabase()
    filtered_grades = filter_grades()

    return render(request, 'catalog.html', context={
        'grades': json.dumps(filtered_grades),
        'concepts': json.dumps({c:l.concepts[c] for c in l.concepts.keys() if l.concepts[c]['public']}),
        'tasks': json.dumps(l.tasks),
        'session': json.dumps(get_session_data(session_id), default=date_converter),
    })


def get_tasks(request):
    data = {}

    task_groups_list = []
    for task, count in request.GET.items():
        method = getattr(l, task, "__none")
        if method != "__none":
            tg_dict = {}
            tg_dict['task_code'] = task
            tg_dict['note'] = ""
            texts_list = []
            for i in range(int(count)):
                text, answer = method()
                texts_list.append((text, answer, ""))
            tg_dict['texts'] = texts_list
            t = m.Task.objects.get(code=task)
            tg_dict['tlt'] = t.tlt
            task_groups_list.append(tg_dict)

    data['tasks'] = task_groups_list

    return JsonResponse(data)


def get_next_student(request):
    s = request.GET['student']
    st = m.Student.objects
    if s != "":
        st = st.filter(login=s)
    st = st.exclude(session__date__exact = datetime.datetime.now().date()).first()

    data = {'login': st.login, 'name': st.name} if st is not None else {'login': "", 'name': ""}

    return JsonResponse(data)


def get_view_session(request, session):
    return render(request, 'viewsession.html', context={
        'session': json.dumps(get_session_data(session), default=date_converter),
    })


def add_session(request):
    data = json.loads(request.body.decode('utf-8'))

    # Создаем сессию
    st = m.Student.objects.filter(login = data['session']['student_login']).first()
    s = m.Session(student=st, note=data['session']['note'])
    s.save()


    groups = data['session']['groups']
    # Создаем группы
    for i, task_dict in enumerate(groups):
        task = m.Task.objects.get(code=task_dict['task_code'])
        tg = m.TaskSessionGroup(session=s, task=task, order=i, note=task_dict['note'])
        tg.save()

        # Создаем тексты
        texts = groups[i]['texts']
        for i, txt in enumerate(texts):
            t = m.TaskText(group=tg, text=txt[0], atext=txt[1], order=i+1)
            t.save()

    response = {'session': s.id}
    return JsonResponse(response)