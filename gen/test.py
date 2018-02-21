import gen.genutils.math_rnd as mrnd
import gen.genutils.math_text as mtxt
import gen.genutils.math_factors as mf
import gen.genutils.math_polynomial as pol
import random as rnd
import math

MODE_GET = 0
MODE_PROGRAM = 1

#---- SETTIGNS------
MODE = MODE_GET
GET_COUNT = 5
EXAMPLES_COUNT = 3
#---- SETTIGNS------

# -----INSERTION START----------------------

tasks = [
	{'kakie_iz_chisel_yavlyayutsya_otritstalnyimi_polozhitelnyimi_neotritsatelnyimi_i_nepolozhitelnyimi': {'tlt': 'Какие из чисел являются отрицтальными, положительными, неотрицательными и неположительными'}},
	{'kakie_iz_chisel_nepolozhitelnyie': {'tlt': 'какие из чисел неположительные'}},
	{'kakie_iz_chisel_neotritstalnyie': {'tlt': 'какие из чисел неотрицтальные'}},
	{'kakie_iz_chisel_polozhitelnyie': {'tlt': 'какие из чисел положительные'}},
	{'kakie_iz_chisel_otritsatelnyie': {'tlt': 'какие из чисел отрицательные'}},
]

def kakie_iz_chisel_yavlyayutsya_otritstalnyimi_polozhitelnyimi_neotritsatelnyimi_i_nepolozhitelnyimi():
# Какие из чисел являются отрицтальными, положительными, неотрицательными и неположительными: 3; -6; -2и1/3; 4,7; 9/16; 0; -5,2; 10,14; 5/8
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), \
        "положительные: " + " ".join([x[0] for x in res if 'положительные' in x[1]]) + "; " + \
        "отрицательные: " + " ".join([x[0] for x in res if 'отрицательные' in x[1]]) + "; " + \
        "неположительные: " + " ".join([x[0] for x in res if 'неположительные' in x[1]]) + "; " + \
        "неотрицательные: " + " ".join([x[0] for x in res if 'неотрицательные' in x[1]]) + "; "


def kakie_iz_chisel_nepolozhitelnyie():
# какие из чисел неположительные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'неположительные' in x[1]])


def kakie_iz_chisel_neotritstalnyie():
# какие из чисел неотрицтальные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'неотрицательные' in x[1]])



def kakie_iz_chisel_polozhitelnyie():
# какие из чисел положительные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'положительные' in x[1]])


def kakie_iz_chisel_otritsatelnyie():
# какие из чисел отрицтальные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'отрицательные' in x[1]])

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

