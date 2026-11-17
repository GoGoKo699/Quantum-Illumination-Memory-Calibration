#!/usr/bin/env python3
"""Check the integer implementation against independent combinatorial laws."""
from fractions import Fraction
from math import comb
from receiver import conditional_pvalue, decide, threshold_bits


def main():
    checks = 0
    for modes in (20, 23, 100, 1000000):
        for total in range(24):
            denominator = comb(total + modes - 1, modes - 1)
            for bright in range(total + 1):
                p = Fraction(comb(total - bright + modes - 1, modes - 1), denominator)
                assert conditional_pvalue(modes, bright, total - bright) == p
                for kappa in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
                    j = threshold_bits(modes, kappa)
                    assert decide(modes, kappa, bright, total - bright) == (p <= Fraction(1, 2**j))
                    checks += 1
    # Distribution-free false-alarm control is checked directly at finite totals.
    for modes in (20, 23, 100):
        for total in range(32):
            denominator = comb(total + modes - 1, modes - 1)
            for j in range(1, 9):
                probability = sum(
                    Fraction(comb(total - k + modes - 2, modes - 2), denominator)
                    for k in range(total + 1)
                    if conditional_pvalue(modes, k, total - k) <= Fraction(1, 2**j)
                )
                assert probability <= Fraction(1, 2**j)
                checks += 1
    print(f'PASS: {checks} exact integer/combinatorial receiver checks')


if __name__ == '__main__':
    main()
