#!/usr/bin/env python3
import PyPDF2
import math


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.div = math.gcd(self.num, self.den)
        self.decimal = self.num / self.den

    def simplifier(self):
        self.den //= self.div
        self.num //= self.div
        return self.num, self.den


pdf = open("DM1 - Sujets_Eleves.pdf", "rb")
pdf = PyPDF2.PdfFileReader(pdf)

for i in range(35):
    page = pdf.getPage(i).extractText().split("\n")

    print(page[2])
    # Exercice 1
    print("Exercice 1:")
    print(page)
    fonction = page[page.find('f'):page.index("sousformecanonique")]
    print(fonction)
    a = b = c = 0
    n = 0
    if fonction[3][-1].isdigit():

        a = int(fonction[3][-1])
        n = 6
    else:
        a = -int(fonction[5])
        n = 8

    if fonction.count("x") == 3:
        if fonction[n] == "":
            if fonction[n + 1] != "x":
                b = -int(fonction[n + 1])
                n += 3
            else:
                b = -1
                n += 2
        else:
            if fonction[n] == '+':
                b = 1
                n += 2
            else:

                b = int(fonction[n])
                n += 2

    if fonction[-1] != "x":
        if fonction[n] == "":
            c = -int(fonction[n + 1])
        else:

            c = int(fonction[n])

    if c == 0:
        print(f"\tLa fonction est: {a}x² {'+' if b > 0 else '-'} {'' if abs(b) == 1 else abs(b)}x")
    elif b == 0:
        print(f"La fonction est: {a}x² {'+' if c > 0 else '-'} {abs(c)}")
    else:
        print(
            f"La fonction est: {a}x² {'+' if b > 0 else '-'} {'' if abs(b) == 1 else abs(b)}x "
            f"{'+' if c > 0 else '-'} {abs(c)}")

    alpha = Fraction(-b, (2 * a))
    alpha.simplifier()
    beta = Fraction(-(b ** 2 - 4 * a * c), (4 * a))
    beta.simplifier()

    print(f"La forme canonique de la fonction est: {a}(x-"
          f"({int(alpha.decimal) if alpha.decimal == int(alpha.decimal) else str(alpha.num) + '/' + str(alpha.den)}))²+"
          f"({int(beta.decimal) if beta.decimal == int(beta.decimal) else str(beta.num) + '/' + str(beta.den)})")

    equation = page[page.index("Résoudrel'équationsuivante:") + 1:page.index(".")]

    for j, k in enumerate(equation):

            if k == "":
                equation[j] = "-"

    equation = " ".join(equation)
    part1, part2 = equation.split("=")
    part1 = part1.split(" ")
    part2 = part2.split(" ")
    if "" in part2:
        part2.pop(part2.index(""))

    n = 0

    if part1[0] == "-":
        if part1[1] != "x":
            a = -int(part1[1])
            n = 4
        else:
            a = -1
    else:
        a = int(part1[0])
        n = 3

    if part1.count("x") == 2:
        if part1[n] == "-":
            b = -int(part1[n + 1])
            n += 3
        else:
            b = int(part1[n])
            n += 2

    if part1[n] == "-":
        c = -int(part1[n + 1])
    else:
        c = int(part1[n])

    for j, k in enumerate(part2):
        if k == "x":
            if j >= 2:
                if part2[j - 1] == "-":
                    b -= -1
                else:
                    b -= -int(part2[j - 1])

                if j == 2:
                    if part2[j + 1] == "-":
                        c -= -int(part2[j + 2])
                else:
                    if part2[0] == "-":
                        c -= -int(part2[1])
                    else:
                        c -= int(part2[0])

            else:
                if j == 0:
                    b -= 1
                    if part2[j + 1] == "-":
                        c -= -int(part2[j + 2])
                    else:
                        c -= int(part2[j + 1])
                elif j == 1:
                    if part2[j - 1] == "-":
                        b -= 1
                    else:
                        b -= int(part2[j - 1])

                    if part2[j + 1] == "-":
                        c -= -int(part2[j + 2])
                    else:
                        c -= int(part2[j + 1])

            break

    delta = b ** 2 - 4 * a * c
    if delta > 0:

        x1 = Fraction(int(-b + delta ** 0.5), 2 * a)
        x1.simplifier()
        x2 = Fraction(int(-b - delta ** 0.5), 2 * a)
        x2.simplifier()
        print(
            f"Les solutions de l'équation sont: "
            f"{int(x1.decimal) if x1.decimal == int(x1.decimal) else str(x1.num) + '/' + str(x1.den)}"
            f" et {int(x2.decimal) if x2.decimal == int(x2.decimal) else str(x2.num) + '/' + str(x2.den)}")
    elif delta == 0:
        x0 = Fraction(-b, 2 * a)
        x0.simplifier()
        print(
            f"La solution de l'équation est: "
            f"{int(x0.decimal) if x0.decimal == int(x0.decimal) else str(x0.num) + '/' + str(x0.den)} ")
    else:
        print("L'équation n'a pas de solution")

    # Exercice 2
    print("Exercice 2")
    nb_jetons = int(page[page.index('Dansuneurnecontenantdesjetonsnumérotésde1à') + 1])
    evenement_a = int(page[page.index(':Lenumérotiréestmultiplede') + 1])
    evenement_b = int(page[page.index(':Lenumérotiréestinférieurouégalà') + 1])
    p_a = Fraction(len([i for i in range(1, nb_jetons + 1) if i % evenement_a == 0]), nb_jetons)
    p_a.simplifier()
    p_b = Fraction(evenement_b, nb_jetons)
    p_b.simplifier()
    p_a_inter_b = Fraction(len([i for i in range(1, nb_jetons + 1) if i % evenement_a == 0 if i <= evenement_b]),
                           nb_jetons)
    p_a_inter_b.simplifier()
    p_a_p_b = Fraction(p_a.num * p_b.num, p_a.den * p_b.den)

    p_a_p_b.simplifier()

    print(f"P(A) = {p_a.num}/{p_a.den}")
    print(f"P(B) = {p_b.num}/{p_b.den}")
    print(f"P(AnB) = {p_a_inter_b.num}/{p_a_inter_b.den}")
    print(f"P(A)xP(B) = {p_a_p_b.num}/{p_a_p_b.den}")
    if p_a_p_b.num == p_a_inter_b.num and p_a_p_b.den == p_a_inter_b.den:
        print("Les évènements A et B sont indépendants car P(A)xP(B) est égale à P(AnB)")
    else:
        print("Les évènements A et B ne sont pas indépendants car P(A)xP(B) n'est pas égale à P(AnB)")

    # Exercice 3
    print("Exercice 3")
    arbre = page[page.index("Onconsidèrelasituationdeprobabilitédécriteparl'arbresuivant.") + 1:page.index(
        'Lesrésultatsdescalculsserontarrondisà')]
    p_a = float("0." + arbre[8])
    p_b_sa = float("0." + arbre[4])
    p_b_sab = float("0." + arbre[-2])
    p_ab = round(1 - p_a, 6)
    p_bb_sa = round(1 - p_b_sa, 6)
    p_bb_sab = round(1 - p_b_sab, 6)
    p_ab_inter_b = round(p_ab * p_b_sab, 6)
    p_a_inter_b = round(p_a * p_b_sa, 6)
    p_b = round(p_a_inter_b + p_ab_inter_b, 6)
    print(f"P(A barre) = {p_ab}")
    print(f"Pa(B barre) = {p_bb_sa}")
    print(f"Pa barre(B barre) = {p_bb_sab}")
    print(f"P(A barre n B) est égale à P(A barre)xPa(B) = {p_ab_inter_b}")
    print(f"P(B)=P(A n B)+P(A barre n B) = {p_b}")
    print(f"Pb(A) = P(A n B)/P(B) = {round(p_a_inter_b / p_b, 6)}")

    print("\n")
