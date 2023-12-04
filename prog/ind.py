#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_int_parts(*args):
    '''
    Функция расчета целых частей после последнего отрицательного.
    '''
    if args:
        values = [float(arg) for arg in args]

        found_negative = False
        total_sum = 0
        for arg in values:
            if arg < 0:
                found_negative = True
                total_sum = 0
            elif found_negative:
                total_sum += int(arg)
        return total_sum

    else: 
        return None


def main():
    '''
    Главная функция программы.
    '''
    print(sum_of_int_parts())
    print(sum_of_int_parts(3, -7, -1, 6, 9))
    print(sum_of_int_parts(1, -5, 8, 4, 3, 9))


if __name__ == "__main__":
    main()