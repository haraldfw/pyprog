# coding: utf-8
from math import sqrt, pi

__author__ = 'Harald Floor Wilhelmsen'

radius = 18.0
quadrantarea = pi * radius * radius / 4

def pizza(xvalue):
    return sqrt((radius * radius) - (xvalue * xvalue))


def getarea(step):
    areatotal = 0.0

    start = 0.0

    while areatotal < quadrantarea / 3 :
        trapezoid_1 = pizza(start)

        start += step
        trapezoid_2 = pizza(start)

        area = ((trapezoid_1 + trapezoid_2) / 2.0) * step
        areatotal += area

    print("t found. t = " + str(start))


getarea(0.000001)
