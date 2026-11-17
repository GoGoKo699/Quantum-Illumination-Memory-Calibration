#!/usr/bin/env python3
"""Exact dyadic conditional detector; no floating-point threshold comparison.

The finite-bit variant is proved in science/processing_robustness.md. The
reflectivity is a supplied positive rational no larger than 1/10.
"""
from fractions import Fraction


def conditional_pvalue(modes: int, bright: int, dark: int) -> Fraction:
    if not all(type(x) is int for x in (modes, bright, dark)):
        raise TypeError('mode and count inputs must be integers')
    if modes < 2 or bright < 0 or dark < 0:
        raise ValueError('require modes >= 2 and nonnegative photon counts')
    result = Fraction(1)
    # Cancels the large binomial coefficients before constructing them.
    for i in range(1, bright + 1):
        result *= Fraction(dark + i, dark + modes - 1 + i)
    return result


def threshold_bits(modes: int, reflectivity: Fraction) -> int:
    if type(modes) is not int or modes < 20:
        raise ValueError('the numerical guarantee requires at least 20 modes')
    if not isinstance(reflectivity, Fraction):
        raise TypeError('supply reflectivity as fractions.Fraction')
    if not 0 < reflectivity <= Fraction(1, 10):
        raise ValueError('require 0 < reflectivity <= 1/10')
    value = modes * reflectivity / 13400
    return (value.numerator + value.denominator - 1) // value.denominator


def decide(modes: int, reflectivity: Fraction, bright: int, dark: int) -> bool:
    """True declares target presence; retains every valid count record."""
    j = threshold_bits(modes, reflectivity)
    pvalue = conditional_pvalue(modes, bright, dark)
    return (pvalue.numerator << j) <= pvalue.denominator
