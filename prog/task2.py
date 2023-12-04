#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garmonic_mean(*args):
    if args:
        values = [float(arg) for arg in args]

        reciprocal_sum = sum(1 / arg for arg in values)
        return len(args) / reciprocal_sum
    
    else: 
        return None


def main():
    print(garmonic_mean())
    print(garmonic_mean(3, 7, 1, 6, 9))


if __name__ == "__main__":
    main()