#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_midle(list_of_nums):
    '''
    Функция, которая считает сумму элементов списка
    '''
    if len(list_of_nums) == 1:
        return list_of_nums[0]
    else:
        middle = len(list_of_nums) // 2
        left_half_sum = sum_of_midle(list_of_nums[:middle])
        right_half_sum = sum_of_midle(list_of_nums[middle:])
        return left_half_sum + right_half_sum


def main():
    '''
    Главная функция программы.
    '''
    print(sum_of_midle([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
