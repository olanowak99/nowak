# -*- coding: utf-8 -*-
from point import Point
from point import normalize_angle


def main():
    with open('teksty.txt', 'r') as file:
        data = file.readlines()

    points = {}

    for i in data:
        i = i.strip().split()
        nr, x, y = i

        point = Point(nr, x, y)
        points[nr] = point

    print(points['P1'].get_length(points['P2']))
    print(points['P2'].get_length(points['P3']))
    print(points['P3'].get_length(points['P4']))

    # floatA = 1.125
    # print(round(floatA, 2))


if __name__ == '__main__':
    main()
