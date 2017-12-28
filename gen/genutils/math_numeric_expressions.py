import gen.genutils.common as lgu
import random as rnd


class NumericElement:
    def __init__(self, elements=(), brackets=False):
        self.elements = list(elements)
        self.brackets = brackets
        self.simplified = False

    def simplify(self):
        for i, e in enumerate(self.elements):
            self.elements[i] = e.simplify()

        if self.simplified:
            return self

        element_types = set([type(e) for e in self.elements])
        new_elements = []
        for element_type in element_types:
            elements_to_simplify = [x for x in self.elements if type(x) == element_type]
            new_elements.extend(type(self).get_simplified(elements_to_simplify))

        self.elements = new_elements
        self.simplified = True

        return self.elements[0] if len(self.elements) == 1 else self

    def remove_brackets(self):
        if type(self) == Number:
            return

        for num in self.elements:
            if (type(self) != Sum and type(num) == Sum) or (type(self) == Division and type(num) == Division):
                num.brackets = True
            else:
                num.brackets = False

            if type(num) == Number and num.n < 0 and (type(self) in [Multiply, Division]):
                num.brackets = True

            num.remove_brackets()

# TODO: Сделать упрощение выражений с дробями, например, 4/6 + 1; 2 + 9^1/2 и т.д.

class Number(NumericElement):
    def __init__(self, n, brackets=False):
        super().__init__(elements=(), brackets=brackets)
        self.n = n
        self.simplified = True

    def set_brackets(self, expression):
        if self.brackets:
            return "(" + expression + ")"
        else:
            return expression

    def get_text(self):
        return self.set_brackets(str(self.n))


class Operation(NumericElement):
    def set_brackets(self, expression):
        if self.brackets:
            return "(" + expression + ")"
        else:
            return expression

class CommutativeOperation(Operation):
    pass


class NonCommutativeOperation(Operation):
    def __init__(self, elements=()):
        super().__init__(elements=elements, brackets=True)


class UnaryOperation(Operation):
    def __init__(self, elements=()):
        super().__init__(elements=elements, brackets=True)
        if len(self.elements) != 1:
            raise Exception("Унарные операции принимают только один операнд")

    def get_text(self):
        return self.set_brackets(self.get_symbol() + self.elements[0].get_text())


class BinaryOperation(Operation):
    def get_text(self):
        res = ""
        for i, e in enumerate(self.elements):
            res += e.get_text()
            if i != len(self.elements) - 1:
                res += self.get_symbol(self.elements[i+1])
        return self.set_brackets(res)


class Sum(BinaryOperation, CommutativeOperation):
    def __init__(self, elements=(), brackets=True):
        super().__init__(elements=elements, brackets=brackets)

    @staticmethod
    def get_simplified(elements):
        return [Number(sum([e.n for e in elements]))]

    @staticmethod
    def get_symbol(element=None):
        if element is None:
            return "+"
        else:
            if type(element) == Number:
                return "" if element.n < 0 else "+"
            if type(element) == Sum and type(element.elements[0]) == Number:
                return "" if element.elements[0].n < 0 else "+"
            else:
                return "+"


class Multiply(BinaryOperation, CommutativeOperation):
    @staticmethod
    def get_simplified(elements):
        res = 1
        for e in elements:
            res *= e.n
        return [Number(res)]

    @staticmethod
    def get_symbol(element=None):
        return "*"


class Power(BinaryOperation, NonCommutativeOperation):
    def __init__(self, elements=()):
        super().__init__(elements=elements)

    @staticmethod
    def get_simplified(elements):
        return [Number(pow(elements[0].n, elements[1].n))]

    @staticmethod
    def get_symbol():
        return "^"


class UnaryMinus(UnaryOperation):
    @staticmethod
    def get_simplified(elements):
        return [Number(-elements[0].n)]

    @staticmethod
    def get_symbol():
        return "-"


class BinaryMinus(BinaryOperation, NonCommutativeOperation):
    @staticmethod
    def get_simplified(elements):
        s = sum([x.n for x in elements[1:]])
        return [Number(elements[0].n - s)]

    @staticmethod
    def get_symbol():
        return "-"


class Division(BinaryOperation, NonCommutativeOperation):
    @staticmethod
    def get_simplified(elements):
        d = 1
        for e in elements[1:]:
            d *= e.n
        n = elements[0].n
        n_delimiters = lgu.factoring(n)
        d_delimiters = lgu.factoring(d)
        all_delimiters = list(set(n_delimiters) | set(d_delimiters))
        delimiters_count = [n_delimiters.count(x) - d_delimiters.count(x) for x in all_delimiters]
        new_d = 1
        new_n = 1
        for i, x in enumerate(all_delimiters):
            c = delimiters_count[i];
            if c == 0:
                continue
            if c > 0:
                new_n *= pow(x, c)
            else:
                new_d *= pow(x, (-c))

        if n * d < 0:
            new_n *= -1

        if new_d == 1:
            return [Number(new_n)]
        else:
            return [Division(elements=(Number(new_n), Number(new_d)))]

    @staticmethod
    def get_symbol(element=None):
        return "/"


numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
open_bracket_symbol = "("
close_bracket_symbol = ")"
element_first_possible_symbols = numbers[:-1] + (open_bracket_symbol,)

operation_classes = (Sum, BinaryMinus, Multiply, Division, Power, UnaryMinus)
operation_symbols = [x.get_symbol() for x in operation_classes]


def simplify_fraction(a, b):
    x = Division(elements=(Number(a), Number(b))).simplify()
    return x.elements[0].n, x.elements[1].n

class NumericBuilder:
    @staticmethod
    def build(expression):
        def build_numeric_element(exp):
            # 1. Удаляем ненужные внешние скобки если они есть
            if exp[0] == open_bracket_symbol and exp[-1] == close_bracket_symbol:
                if lgu.get_close_bracket_pos(exp, 0) == len(exp) - 1:
                    exp = exp[1:-1]

            # 2. Составляем список всех элементов выражения
            elements = []
            p = 0
            while p <= len(exp) - 1:
                # Ищем либо цифру, минус либо скобку - с них начинается элемент
                el_start_pos = -1
                for i, symbol in enumerate(exp[p:]):
                    if symbol in element_first_possible_symbols:
                        el_start_pos = p + i
                        break
                el_first_symbol = exp[el_start_pos]
                el_stop_pos = -1

                # Если цифра, то это начало элемента
                if el_first_symbol in numbers:
                    for i, symbol in enumerate(exp[el_start_pos + 1:]):
                        if symbol not in numbers:
                            el_stop_pos = el_start_pos + i
                            break
                    el_stop_pos = len(exp) - 1 if el_stop_pos == -1 else el_stop_pos

                # Если скобка, то ищем ее пару
                if el_first_symbol == open_bracket_symbol:
                    el_stop_pos = lgu.get_close_bracket_pos(exp, p)

                el_str = exp[el_start_pos:el_stop_pos + 1]
                p = el_stop_pos + 1

                # TODO: Убрать сохранение строк элементов (были нужно для наглядности отладки)
                elements.append((el_str, el_start_pos, el_stop_pos))

            # 3. Составляем список всех операций в выражении. Каждая операция имеет элементы, на которые она действ-ет
            operations = []

            # Смотрим есть ли унарная операция
            unary_operation_symbols = [x.get_symbol() for x in operation_classes if issubclass(x, UnaryOperation)]
            first_operation_symbol = set(unary_operation_symbols) & set(exp[0:elements[0][1]])
            if len(first_operation_symbol) > 0:
                elements = [('', 0, 0)] + elements

            # Перебираем пары элементов и определяем операции между ними
            for el1, el2 in zip(elements, elements[1:]):
                operation_symbol = list(set(operation_symbols) & set(exp[el1[2]:el2[1]]))[0]
                if len(operation_symbol) > 0:
                    possible_operation_classes = [x for x in operation_classes if x.get_symbol() == operation_symbol]
                    if len(possible_operation_classes) == 1:
                        operation_class = possible_operation_classes[0]
                    else:
                        if len(el1[0]) == 0:
                            operation_class = [x for x in possible_operation_classes if issubclass(x, UnaryOperation)][0]
                        else:
                            operation_class = [x for x in possible_operation_classes if issubclass(x, BinaryOperation)][0]
                    operations.append((operation_class, el1, el2),)
                else:
                    raise lgu.TextParseException("Неизвестные символы операций")

            # 4. Составляем список операций выражения, которые являются операциями верхнего уровня
            main_operation = None
            for operation in operation_classes:
                if operation in [op[0] for op in operations]:
                    main_operation = operation
                    break
            main_operations = [op for op in operations if op[0] == main_operation]

            # 5. Составляем список операндов главных операций выражения
            main_elements = []
            if len(operations) != 0:
                if issubclass(main_operation, UnaryOperation):
                    main_elements.append(main_operations[0][2])
                else:
                    start_pos = 0
                    for i, operation in enumerate(main_operations):
                        end_pos = operation[1][2]
                        main_elements.append((exp[start_pos:end_pos + 1], start_pos, end_pos))
                        start_pos = operation[2][1]
                        if i == len(main_operations) - 1:
                            end_pos = len(exp) - 1
                            main_elements.append((exp[start_pos:end_pos + 1], start_pos, end_pos))
            else:
                if len(elements) == 1:
                    main_elements.append(elements[0])

            # Debug output
            print(str(main_operation) + str([e[0] for e in main_elements]))

            # 6. Запускаем рекурсию на каждый операнд каждой операции верхнего уровня или возвращаем число
            if main_operation is not None:
                els = [build_numeric_element(el[0]) for el in main_elements]
                return main_operation(elements=els)
            else:
                return Number(int(main_elements[0][0]))

        return build_numeric_element(expression)

def spread_out(number, cur_depth, max_depth):
    if cur_depth > max_depth:
        return number

    operation = rnd.randint(0, 10)

    c = rnd.randint(2, 3)
    t = number.n

    # Сумма
    if operation in [0, 1, 2, 3, 4, 5]:
        s = rnd.randint(-30, 30)
        ms = [s]
        for i in range(c - 1):
            if i == c - 2:
                m = t - s
            else:
                if s < t:
                    m = rnd.randint(1, 30)
                else:
                    m = rnd.randint(-30, -1)
            ms.append(m)
            s += m

        elements = [Number(x) for x in ms]
        number = Sum(elements=elements)

    # Произведение
    if operation in [6, 7]:
        f = lgu.factoring(t)
        f = f[1:]
        rnd.shuffle(f)
        if t < 0:
            f[0] = -f[0]
        if len(f) > 1:
            elements = [Number(x) for x in f]
        else:
            if rnd.randint(0, 3) == 0:
                elements = None
            else:
                elements = [Number(f[0]), Number(1)]
        if elements != None:
            number = Multiply(elements=elements)

    # Деление
    if operation in [8, 9, 10]:
        denumerator = rnd.randint(2, 10)
        numerator = t * denumerator
        elements = (Number(numerator), Number(denumerator))
        number = Division(elements=elements)

    if elements != None:
        c = len(elements)
        r = rnd.randint(1, c - 1)
        rs = rnd.sample(range(c), r)
        for i in rs:
            number.elements[i] = spread_out(elements[i], cur_depth + 1, max_depth)

    return number


# expression = "4/6"
# print(expression)
# ns = NumericBuilder.build(expression)
# print(ns.get_text())
# ns.simplify()
# print(ns.get_text())
