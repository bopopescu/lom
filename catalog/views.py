from django.shortcuts import render
import gen.lib as l
import json
from django.http import JsonResponse

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
    import catalog.models as cModels

    l.grades = {}
    l.concepts = {}
    l.tasks = {}
    l.task_order_in_concept = {}

    for t in cModels.Task.objects.all():
        if getattr(l, t.code, "__none") != "__none":
            ex = t.example.replace("'", "")
            ex = (ex[:100] + '..') if len(ex) > 100 else ex
            l.tasks[t.code] = {'title': t.tlt, 'example': ex}
            l.tasks[t.code]['orders'] = {}

    for c in cModels.Concept.objects.all():

        tasks_array = []
        for t in c.tasks.all():
            if t.code in l.tasks:
                tic = cModels.TaskInConcept.objects.get(task=t, concept=c)
                order = tic.order
                tasks_array.append((t.code, order))

        def get_task_order(t1):
            t_code, t_order = t1
            return t_order

        tasks_array = sorted(tasks_array, key=get_task_order, reverse=False)

        if len(tasks_array) > 0:
            l.concepts[c.code] = {'public': c.public, 'title': c.tlt}
            l.concepts[c.code]['tasks'] = [t_code for t_code, t_order in tasks_array]

    for g in cModels.Grade.objects.all():
        l.grades[g.code] = {'title': g.tlt}
        concepts_array = []
        for c in g.concepts.all():
            if c.code in l.concepts:
                concepts_array.append(c.code)
        l.grades[g.code]['concepts'] = concepts_array


def index(request):
    updateParamsFromDatabase()

    filtered_grades = filter_grades();
    return render(request, 'catalog.html', context={
        'grades': json.dumps(filtered_grades),
        'concepts': json.dumps({c:l.concepts[c] for c in l.concepts.keys() if l.concepts[c]['public']}),
        'tasks': json.dumps(l.tasks),
        'concept_id': '',
        'tasks_group': '',
        'session': '',
        'user': '',
    })


def get_session(request, session):
    updateParamsFromDatabase()
    filtered_grades = filter_grades();

    from catalog.models import Session, TaskInSession
    if Session.objects.filter(pk=session).exists():
        session_obj = Session.objects.get(pk=session)
        student_name = session_obj.student.name

        tasks_array = []
        for t in session_obj.tasks.all():
            if t.code in l.tasks:
                tis = TaskInSession.objects.get(task=t, session=session_obj)
                order = tis.order
                count = tis.count
                tasks_array.append((t.code, order, count))

            def get_task_order(t1):
                t_code, t_order, t_count = t1
                return t_order

        tasks_array = sorted(tasks_array, key=get_task_order, reverse=False)

        session_data = {'tasks': tasks_array}
    else:
        student_name = ""
        session_data = {'tasks': []}


    return render(request, 'catalog.html', context={
        'grades': json.dumps(filtered_grades),
        'concepts': json.dumps({c:l.concepts[c] for c in l.concepts.keys() if l.concepts[c]['public']}),
        'tasks': json.dumps(l.tasks),
        'concept_id': json.dumps(request.GET.get('concept', None)),
        'tasks_group': '',
        'session': json.dumps(session_data),
        'user': json.dumps(student_name),
    })


def get_concept(request):
    updateParamsFromDatabase()

    c = request.GET.get('concept', None)
    filtered_grades = filter_grades();

    return render(request, 'catalog.html', context={
        'grades': json.dumps(filtered_grades),
        'concepts': json.dumps({c:l.concepts[c] for c in l.concepts.keys() if l.concepts[c]['public']}),
        'tasks': json.dumps(l.tasks),
        'concept_id': json.dumps(request.GET.get('concept', None)),
        'tasks_group': '',
        'session': '',
        'user': '',
    })


def get_tasks_group(request):
    updateParamsFromDatabase()

    params = request.GET.dict()
    filtered_grades = filter_grades();
    return render(request, 'catalog.html', context={
        'grades': json.dumps(filtered_grades),
        'concepts': json.dumps({c:l.concepts[c] for c in l.concepts.keys() if l.concepts[c]['public']}),
        'tasks': json.dumps(l.tasks),
        'tasks_group': json.dumps(params, None),
        'concept_id': '',
        'session': '',
        'user': '',
    })


def get_tasks(request):
    data = {}
    data['tasks'] = {}

    for task, count in request.GET.items():
        method = getattr(l, task, "__none")
        if method != "__none":
            new_tasks = []
            for i in range(int(count)):
                task_text, answer_text = method()
                new_tasks += [task_text]
            data['tasks'][task] = new_tasks

    return JsonResponse(data)