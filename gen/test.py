import gen.genutils.math_rnd as mrnd
import gen.genutils.math_text as mtxt
import gen.genutils.math_factors as mf
import gen.genutils.math_polynomial as pol
import random as rnd
import math
import gen.genutils.math_trig as tr

MODE_GET = 0
MODE_PROGRAM = 1

#---- SETTIGNS------
MODE = MODE_PROGRAM
GET_COUNT = 1
EXAMPLES_COUNT = 3
#---- SETTIGNS------

# -----INSERTION START----------------------

tasks = [
	{'vyichislite659': {'tlt': 'Вычислите'}},
]

def vyichislite659():
# Вычислите arccos(cos(+/-9)) // тоже самое с arcsin
    c = 0#rnd.randint(0, 1)
    x = mrnd.rnd_w(-10, 10, [0])

    # Определяем в какой четверти лежит угол x
    xgrad = x * 180 / math.pi
    ch360 = int(xgrad) % 360
    if ch360 > 0:
        ch = 1 if ch360 < 90 else (2 if ch360 < 180 else (3 if ch360 < 270 else 4))
    else:
        ch = 4 if -ch360 < 90 else (3 if -ch360 < 180 else (2 if -ch360 < 270 else 1))

    def get_n(a):
        if a > 0:
            return int(a // 1)
        else:
            return -int((-a + 1) // 1)

    answer = ""
    if c == 0:
        if ch in [1, 2]:
            n = get_n(x/(2 * math.pi))
            answer = str(x) + ((mtxt.fc(int(-2 * n), False) + "pi") if n != 0 else "")
        if ch == 3:
            n = get_n(x/(4 * math.pi) - 1/4)
            nsh = get_n(x/(2 * math.pi) - 1/2 - 2 * n)
            answer = ((mtxt.fc(int(2 + 4 * n + 2 * nsh)) + "pi") if ((2 + 4 * n + 2 * nsh) != 0) else "") + mtxt.s(-x)
        if ch == 4:
            n = get_n(x/(4 * math.pi) + 1/8)
            nsh = get_n(x/(2 * math.pi) + 1/4 - 2 * n)
            answer = ((mtxt.fc(int(4 * n + 2 * nsh)) + "pi") if (4 * n + 2 * nsh != 0) else "") + mtxt.s(-x)

    if c == 1:
        if ch in [4, 1]:
            n = get_n(x/(2 * math.pi))
            answer = str(x) + mtxt.fc(int(-2 * n), False) + "pi"
        if ch == 2:
            pass
        if ch == 3:
            pass


    return ("arccos" if c == 0 else "arcsin") + mtxt._(("cos" if c == 0 else "sin") + mtxt._(x)), \
          answer


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