import random as rnd

def common_base_power():
    n = rnd.randint(2, 10)
    if n in [6, 7, 8, 9, 10]:
        k = 2
    if n in [3, 4, 5]:
        k = rnd.randint(2, 3)
    if n in [2, 3]:
        k = rnd.randint(2, 5)
    if n in [2]:
        k = rnd.randint(2, 10)
    return n, k

def rnd_w0(min, max):
    return rnd.choice(list(range(min, 0)) + list(range(1, max + 1)))

def rnd_w(min, max, exc=[]):
    ch = list(range(min, max + 1))
    return choice_w(ch, exc)

def choice_w(choices, exc=[]):
    ch = choices
    for e in exc:
        if e in ch:
            ch.remove(e)
    return rnd.choice(ch)
