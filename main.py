# -*- coding: utf-8 -*-
from point import Point
from point import normalize_angle


def main():
    with open('teksty.txt', 'r') as file:
        data = file.readlines()

    print(data)
    print(type(data))

    for line in data:
        print(line.strip().upper().split())


if __name__ == '__main__':
    main()
