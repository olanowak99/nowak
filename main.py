# -*- coding: utf-8 -*-
from point import Point
from point import normalize_angle


def main():
    with open('teksty.txt', 'r') as file:
        data = file.readlines()

    points = []

    for line in data:
        nr, x, y = line.strip().split()
        point = Point(nr, x, y)
        points.append(point)

    sum_all_azimuth = 0
    for i in range(len(points)-2):
        i = i+1
        # sum_all_azimuth += points[i].get_azimuth(points[i + 1])
        sum_all_azimuth += points[i].get_angle(points[i + -1], points[i+1])

    print(sum_all_azimuth)


if __name__ == '__main__':
    main()
