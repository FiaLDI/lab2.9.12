#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*args):
    if args:
        values = [float(arg) for arg in args]

        value = 1
        for arg in values:
            value *= arg
        return value ** (1 / len(values))
    
    else: 
        return None


def main():
    print(geometric_mean())
    print(geometric_mean(3, 7, 1, 6, 9))


if __name__ == "__main__":
    main()