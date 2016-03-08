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
        value1 = pizza(start)
        start += step / 2
        value2 = pizza(start)
        area = ((value1 + value2) / 2.0) * step / 2
        areatotal += area

        #print("processing s " + str(start))

    print("t found. t = " + str(start))


getarea(0.000001)
