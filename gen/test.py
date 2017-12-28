import gen.genutils.math_rnd as mrnd
import gen.genutils.math_text as mtxt
import gen.genutils.math_factors as mf
import random as rnd

MODE_GET = 0
MODE_PROGRAM = 1

#---- SETTIGNS------
MODE = MODE_PROGRAM
GET_COUNT = 10
EXAMPLES_COUNT = 3
#---- SETTIGNS------

# -----INSERTION START----------------------

tasks = [
	{'postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij445': {'tlt': 'Построй в одной системе координат графики функций'}},
	{'kakovyi_oblast_opredelenij_i_oblast_znachenij_funktsii444': {'tlt': 'каковы область определений и область значений функции'}},
	{'postroj_v_odnoj_sisteme_koordinat_grafiki_funktsii': {'tlt': 'построй в одной системе координат графики функции'}},
	{'kakaya_iz_funktsii_lezhit': {'tlt': 'какая из функции быстрее'}},
	{'vozrastaet_ili_ubyivaet_funktsiya441': {'tlt': 'возрастает или убывает функция'}},
]

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij445():
    # Построй в одной системе координат графики функций:  y = x^-2, y = x^-3 и y = x^-4
    k_min = 2 * rnd.randint(1, 4)

    return "y=x^-" + str(k_min) + ", y=x^-" + str(k_min + 1) + " и y=x^-" + str(k_min + 2), ''

def kakovyi_oblast_opredelenij_i_oblast_znachenij_funktsii444():
    # каковы область определений и область значений функции y = x^-3 (n=[0, 10])
    k = rnd.randint(2, 9)
    return "какова область определения и область значений функции y=x^-" + str(k), \
           "область определения: вся числовая ось, область значений: " + (
           "любое число" if k % 2 != 0 else "[0, +бесконечность]")

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsii():
    # построй в одной системе координат графики функции y = x^-2 и y = x^-4
    if rnd.randint(0, 1) == 0:
        k1 = 2 * rnd.randint(1, 4)
        k2 = 2 * mrnd.rnd_w(1, 4, [k1])
    else:
        k1 = 2 * rnd.randint(1, 4) + 1
        k2 = 2 * mrnd.rnd_w(1, 4, [k1]) + 1

    return "построй в одной системе координат графики функций: y=x^-" + str(k1) + " и y=x^-" + str(k2), ''

def kakaya_iz_funktsii_lezhit():
    # какая из функции быстрее: убывает|возрастает на отрезке (-бесконечность, -1) | (-1, 0) | (0, 1) | (1, +бесконечность) y = x^-2 или x^-4
    uc = rnd.randint(0, 3)
    uv = rnd.randint(0, 1)
    k1 = rnd.randint(2, 9)
    k2 = mrnd.rnd_w(2, 9, [k1])

    if uc == 0:
        ucs = "(-бесконечность, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +бесконечность)"

    uvs = ("выше" if uv == 0 else "ниже")

    f1 = "y=x^-" + str(k1)
    f2 = "y=x^-" + str(k2)

    if uc == 0:
        if uv == 0:
            answer = f1 if (k1 % 2 == 0 and k2 % 2 != 0) or ((k1 % 2 == 0 and k2 % 2 == 0) and k1 < k2) else f2
        if uv == 1:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 != 0 and k2 % 2 != 0) and k1 < k2) else f2
    if uc == 1:
        if uv == 0:
            answer = f1 if (k1 % 2 == 0 and k2 % 2 != 0) or ((k1 % 2 == 0 and k2 % 2 == 0) and k1 > k2) else f2
        if uv == 1:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 != 0 and k2 % 2 != 0) and k1 > k2) else f2
    if uc == 2:
        if uv == 0:
            answer = f1 if k1 > k2 else f2
        if uv == 1:
            answer = f1 if k1 < k2 else f2
    if uc == 3:
        if uv == 0:
            answer = f1 if k1 < k2 else f2
        if uv == 1:
            answer = f1 if k1 > k2 else f2

    return uvs + " на отрезке " + ucs + ": " + f1 + " или " + f2, answer

def vozrastaet_ili_ubyivaet_funktsiya441():
# y = x^-3 на участке (-бесконечность, -1) | (-1, 0) | (0, 1) | (1, +бесконечность)
    uc = rnd.randint(0, 3)
    k = rnd.randint(2, 9)

    if uc == 0:
        ucs = "(-бесконечность, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +бесконечность)"

    if k % 2 == 0:
        answer = "возрастает " if uc not in [2, 3] else "убывает"
    else:
        answer = "убывает"

    return "y=x^-" + str(k) + " на участке " + ucs, answer

# -----INSERTION END-----------------------


if MODE == MODE_GET:
    import mysql.connector
    import sshtunnel

    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='kostbash', ssh_password='Kost874Bash854',
        remote_bind_address=('kostbash.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = mysql.connector.connect(
            user='kostbash', password='aJi^_!3Bfg7(_)',
            host='127.0.0.1', port=tunnel.local_bind_port,
            database='kostbash$lom',
        )

        # Получаем данные с prod базы
        cursor = connection.cursor()
        GET_TASKS_SQL = "SELECT code, tlt FROM catalog_task ORDER BY catalog_task.id DESC LIMIT {}".format(GET_COUNT)
        GET_CONCEPT_SQL = "SELECT code FROM catalog_concept ORDER BY catalog_concept.id DESC LIMIT {}".format(1)
        cursor.execute(GET_TASKS_SQL)
        tasks = cursor.fetchall()
        cursor.close()
        cursor = connection.cursor()
        cursor.execute(GET_CONCEPT_SQL)
        con = cursor.fetchall()

        # Формируем строку списка тасков
        code = "tasks = [" + "\n"
        for c, t in tasks:
            code += "\t" + "{'" + c + "': {'tlt': '" + t + "'}}," + "\n"
        code += "]\n\n"

        # Дополняем строку шаблонами функций

        for c, t in tasks:
            code += "def " + c + "():\n\treturn '', '' \n\n"

        connection.close()
        print('http://lomonosov.xyz/concept/?concept=' + con[0][0])
        print(code)

if MODE == MODE_PROGRAM:
    import sys
    text = ""
    for i, t in enumerate(tasks):
        task_code = list(t.keys())[0]
        text += str(i + 1) + ". " + t[task_code]['tlt'] + ":\n"
        for j in range(0, EXAMPLES_COUNT):
            method = getattr(sys.modules[__name__], task_code)
            task_text, answer_text = method()
            text += "\t" + str(j + 1) + ". " + task_text + "\n" + "Ответ: " + answer_text + "\n"
    print(text)

