import gen.genutils.common as lgu
import random as rnd


class GenException(Exception):
    pass


class MonomialSumException(GenException):
    pass


class Monomial():
    def __init__(self, c=1, p=0):
        self.coefficient = c
        self.power = p

    @staticmethod
    def product(monomials):
        coefficient = 1
        power = 0
        for monomial in monomials:
            coefficient *= monomial.coefficient
            power += monomial.power
        return Monomial(coefficient, power)

    def set_product(self, monomials):
        m = Monomial.product(monomials)
        self.coefficient = m.coefficient
        self.power = m.power

    @staticmethod
    def sum(monomials):
        monomials_set = set([m.power for m in monomials])
        if len(monomials_set) != 1:
            raise MonomialSumException("Нельзя суммировать одночлены с разными степенями и получить одночлен")

        coefficient = 0
        for monomial in monomials:
            coefficient += monomial.coefficient
            power = list(monomials_set)[0]

        return Monomial(coefficient, power)

    def set_sum(self, monomials):
        m = Monomial.sum(monomials)
        self.coefficient = m.coefficient
        self.power = m.power

    def get_str(self, is_first = True):
        return lgu.get_one_member_str(self.coefficient, self.power, is_first)

    def generate(self):
        pass

    def clear(self):
        pass


class Polynomial():
    def __init__(self, coefficients = [], powers = [], monomials = []):
        if len(monomials) == 0:
            self.set_by_cp(coefficients, powers)
        else:
            self.monomials = monomials

    def set_by_cp(self, coefficients = [], powers = []):
        self.monomials = [Monomial(m[0], m[1]) for m in zip(coefficients, powers)]

    def get_c_by_p(self, p):
        for m in self.monomials:
            if m.power == p:
                return m.coefficient
        return None

    @staticmethod
    def simplify(monomials):
        res_monomials = []
        for p in set([m.power for m in monomials]):
            res_monomials.append(Monomial.sum([m for m in monomials if m.power == p]))
        return Polynomial(monomials=res_monomials)

    @staticmethod
    def __product_2p(polynomial1, polynomial2):
        monomials = []
        for m1 in polynomial1.monomials:
            for m2 in polynomial2.monomials:
                monomials.append(Monomial.product([m1, m2]))
        return Polynomial.simplify(monomials=monomials)

    @staticmethod
    def product(polynomials):
        if len(polynomials) == 0:
            return Monomial()

        if len(polynomials) == 1:
            return polynomials[0]

        for i, p in enumerate(polynomials):
            if i == 0:
                p1 = polynomials[0]
                continue
            p2 = polynomials[i]
            pol = Polynomial.__product_2p(p1, p2)
            p1 = pol

        return pol

    @staticmethod
    def sum(polynomials):
        monomials = []
        for p in polynomials:
            monomials.extend(p.monomials)

        return Polynomial.simplify(monomials)

    def get_str(self, shuffle=False):
        res = ""
        ms = self.monomials
        if shuffle:
            rnd.shuffle(ms)
        for i, m in enumerate(ms):
            res += m.get_str(i == 0)
        return res

    def clear(self):
        self.monomials = []

    def get_replaced_str(self, replacements={}):
        if len(replacements) == 0:
            return self.get_str()
        else:
            res = ""
            for i, m in enumerate(self.monomials):
                if i not in replacements.keys():
                    res += m.get_str(i == 0)
                else:
                    new_power = m.power - 1 if m.power != 0 else m.power
                    new_monomial = Monomial(m.coefficient, new_power)
                    pol = replacements[i]
                    res += new_monomial.get_str(i==0) + "(" + pol.get_str() + ")"
            return res

def get_str(coeffs, powers):
    return Polynomial(coefficients=coeffs, powers=powers).get_str()

# class QuadraticPolynomialType(Enum):
#     BY_ROOTS = 1
#     BY_DISCRIMINATOR = 2
#     BY_COEFFICIENTS = 3
#
#
# class QuadraticPolynomial(Polynomial):
#     def __init__(self):
#         super().__init__()
#         self.discriminator = 0
#         # self.x1 = Fraction(1, 1)
#         # self.x2 = Fraction(1, 1)
#         self.a = 1
#         self.b = 2
#         self.c = -1
#         self.generation_type = QuadraticPolynomialType.BY_ROOTS
#
#     def generate(self):
#         if self.generation_type == QuadraticPolynomialType.BY_ROOTS:
#             p1 = Polynomial([self.x1.denumerator, -self.x1.numerator], [1, 0])
#             p2 = Polynomial([self.x2.denumerator, -self.x2.numerator], [1, 0])
#             self.monomials = Polynomial.product([p1, p2]).monomials
#
#         if self.generation_type == QuadraticPolynomialType.BY_DISCRIMINATOR:
#             pass
#
#         if self.generation_type == QuadraticPolynomialType.BY_COEFFICIENTS:
#             self.set_by_cp([self.a, self.b, self.c], [2, 1, 0])
