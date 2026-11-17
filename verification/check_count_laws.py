#!/usr/bin/env python3
"""Deterministic checks of the conditional-count receiver.

Exact rational checks cover finite count coefficients and conditional null laws.
The finite-parameter probability sums are numerical diagnostics with explicit
Chernoff truncation bounds; they are not a replacement for the written theorem.
Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


def negative_binomial_mass(shape: int, mean: Fraction, count: int) -> Fraction:
    return (
        Fraction(math.comb(count + shape - 1, count))
        * mean**count
        / (1 + mean) ** (shape + count)
    )


def bright_coefficients_exact(
    modes: int, memory_mean: Fraction, displacement: Fraction, cutoff: int
) -> list[Fraction]:
    """Coefficients of (1+e(1-t))^(N-1)/(1+m(1-t))^N."""
    residual = memory_mean - displacement
    p = memory_mean / (1 + memory_mean)
    q = residual / (1 + residual)
    coefficients = [(1 + residual) ** (modes - 1) / (1 + memory_mean) ** modes]
    derivative_coefficients = [
        modes * p ** (j + 1) - (modes - 1) * q ** (j + 1)
        for j in range(cutoff)
    ]
    for k in range(cutoff):
        coefficients.append(
            sum(
                derivative_coefficients[j] * coefficients[k - j]
                for j in range(k + 1)
            )
            / (k + 1)
        )
    return coefficients


def conditional_tail_exact(modes: int, total: int, bright: int) -> Fraction:
    return Fraction(
        math.comb(total - bright + modes - 1, modes - 1),
        math.comb(total + modes - 1, modes - 1),
    )


def check_exact_count_identities() -> dict:
    coefficient_checks = 0
    conditional_checks = 0
    superuniform_checks = 0
    cutoff = 24
    for modes in (2, 3, 5, 8):
        for memory, displacement in (
            (Fraction(1, 5), Fraction(0)),
            (Fraction(1, 5), Fraction(1, 20)),
            (Fraction(2, 3), Fraction(1, 7)),
        ):
            residual = memory - displacement
            bright = bright_coefficients_exact(modes, memory, displacement, cutoff)
            assert all(value >= 0 for value in bright)
            dark = [negative_binomial_mass(modes - 1, residual, k) for k in range(cutoff + 1)]
            for total in range(cutoff + 1):
                convolution = sum(bright[k] * dark[total - k] for k in range(total + 1))
                expected = negative_binomial_mass(modes, memory, total)
                assert convolution == expected
                coefficient_checks += 1
        for total in range(cutoff + 1):
            denominator = math.comb(total + modes - 1, modes - 1)
            probabilities = [
                Fraction(math.comb(total - k + modes - 2, modes - 2), denominator)
                for k in range(total + 1)
            ]
            assert sum(probabilities) == 1
            tails = [conditional_tail_exact(modes, total, k) for k in range(total + 1)]
            for k in range(total + 1):
                assert tails[k] == sum(probabilities[k:])
                conditional_checks += 1
            levels = {Fraction(j, 20) for j in range(21)} | set(tails)
            for level in levels:
                rejection_probability = sum(
                    probability
                    for probability, pvalue in zip(probabilities, tails)
                    if pvalue <= level
                )
                assert rejection_probability <= level
                superuniform_checks += 1
    return {
        "exact_pgf_convolution_coefficients_checked": coefficient_checks,
        "exact_conditional_survival_probabilities_checked": conditional_checks,
        "exact_discrete_superuniformity_inequalities_checked": superuniform_checks,
        "largest_total_photon_number_checked": cutoff,
    }


def check_phase_geometry() -> dict:
    vectors = (
        (1 + 2j, -3 + 1j),
        (0j, 2j, 3 - 1j, -1 + 4j),
        (1 + 0j,) * 7,
    )
    checks = 0
    for record in vectors:
        norm_squared = sum(abs(z) ** 2 for z in record)
        norm = math.sqrt(norm_squared)
        row = [z / norm for z in record]
        assert abs(sum(abs(z) ** 2 for z in row) - 1) < 1e-14
        for phase in (0.0, 0.19, 1.7, math.pi, 5.4):
            global_phase = complex(math.cos(phase), math.sin(phase))
            displacement = [global_phase * z.conjugate() for z in record]
            captured = abs(sum(w * d for w, d in zip(row, displacement))) ** 2
            assert abs(captured / norm_squared - 1) < 1e-14
            checks += 1
    return {"deterministic_static_phase_concentration_checks": checks}


def geometric_divergence(observed: float, mean: float) -> float:
    if observed == 0:
        return math.log1p(mean)
    return observed * math.log(observed / mean) - (observed + 1) * math.log1p(
        (observed - mean) / (mean + 1)
    )


def negative_binomial_numerical(shape: int, mean: float, cutoff: int) -> list[float]:
    """Stable mode-centered probabilities, normalized on the finite range."""
    mode = min(cutoff, max(0, math.floor((shape - 1) * mean)))
    p = mean / (1 + mean)
    weights = [0.0] * (cutoff + 1)
    weights[mode] = 1.0
    for k in range(mode, cutoff):
        weights[k + 1] = weights[k] * (shape + k) * p / (k + 1)
    for k in range(mode, 0, -1):
        weights[k - 1] = weights[k] * k / ((shape + k - 1) * p)
    normalizer = math.fsum(weights)
    return [value / normalizer for value in weights]


def bright_numerical(modes: int, memory: float, displacement: float, cutoff: int) -> list[float]:
    residual = memory - displacement
    p = memory / (1 + memory)
    q = residual / (1 + residual)
    coefficients = [math.exp((modes - 1) * math.log1p(residual) - modes * math.log1p(memory))]
    derivative = [modes * p ** (j + 1) - (modes - 1) * q ** (j + 1) for j in range(cutoff)]
    for k in range(cutoff):
        coefficients.append(
            math.fsum(derivative[j] * coefficients[k - j] for j in range(k + 1)) / (k + 1)
        )
    return coefficients


def numerical_error(
    modes: int, memory: float, displacement: float, rate: float, bright_cutoff: int
) -> dict:
    residual = memory - displacement
    dark_cutoff = math.ceil((modes - 1) * memory + 16 * math.sqrt((modes - 1) * memory * (1 + memory)) + 64)
    bright = bright_numerical(modes, memory, displacement, bright_cutoff)
    dark = negative_binomial_numerical(modes - 1, residual, dark_cutoff)
    rejection = 0.0
    acceptance = 0.0
    threshold = -modes * rate
    for s, dark_probability in enumerate(dark):
        log_pvalue = 0.0
        for k, bright_probability in enumerate(bright):
            if k:
                log_pvalue += math.log((s + k) / (s + modes - 1 + k))
            probability = bright_probability * dark_probability
            if log_pvalue <= threshold:
                rejection += probability
            else:
                acceptance += probability
    dark_tail = math.exp(
        -(modes - 1)
        * geometric_divergence((dark_cutoff + 1) / (modes - 1), residual)
    )
    tilt = 1.0
    v = math.expm1(tilt)
    log_mgf = (modes - 1) * math.log1p(-residual * v) - modes * math.log1p(-memory * v)
    bright_tail = min(1.0, math.exp(log_mgf - tilt * (bright_cutoff + 1)))
    return {
        "rejection_probability": rejection,
        "acceptance_probability": acceptance,
        "chernoff_truncation_bound": dark_tail + bright_tail,
        "bright_count_cutoff": bright_cutoff,
        "dark_count_cutoff": dark_cutoff,
        "summed_probability": rejection + acceptance,
    }


def check_finite_probabilities() -> dict:
    n = 0.001
    background = 10.0
    reflectivity = 0.1
    modes = 1_000_000
    u = -math.expm1(-2.0)
    lstar = math.log1p(0.95 / 0.003)
    amin = reflectivity * 0.9 * n * (1 + n) / (background + reflectivity * n + 1)
    cstar = -math.log1p(-amin * u / (1 + 0.002 * u))
    rate = cstar * lstar / (lstar + 2)
    false_alarm_bound = math.exp(-modes * rate)
    risk_bound = 1.5 * false_alarm_bound
    numerical_tolerance = 1e-10
    rows = []
    for eta, added_noise in ((0.9, 0.0), (0.9, 0.001), (1.0, 0.0), (1.0, 0.001), (0.95, 0.0005)):
        memory = eta * n + added_noise
        displacement = reflectivity * eta * n * (1 + n) / (background + reflectivity * n + 1)
        null = numerical_error(modes, memory, 0.0, rate, 160)
        alternative = numerical_error(modes, memory, displacement, rate, 160)
        alpha = null["rejection_probability"]
        beta = alternative["acceptance_probability"]
        omitted = null["chernoff_truncation_bound"] + alternative["chernoff_truncation_bound"]
        risk = (alpha + beta) / 2
        assert abs(null["summed_probability"] - 1) < numerical_tolerance
        assert abs(alternative["summed_probability"] - 1) < numerical_tolerance
        assert alpha + omitted + numerical_tolerance <= false_alarm_bound
        assert beta + omitted + numerical_tolerance <= 2 * false_alarm_bound
        assert risk + omitted + numerical_tolerance <= risk_bound
        rows.append({
            "eta": eta,
            "added_noise": added_noise,
            "false_alarm": alpha,
            "miss_probability": beta,
            "symmetric_risk": risk,
            "chernoff_truncation_bound": omitted,
        })
    return {
        "method": "deterministic count-law sums; double precision; not Monte Carlo",
        "modes": modes,
        "reflectivity": reflectivity,
        "uniform_rate": rate,
        "uniform_false_alarm_bound": false_alarm_bound,
        "uniform_symmetric_risk_bound": risk_bound,
        "floating_point_comparison_tolerance": numerical_tolerance,
        "cases": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="optional path for the verification report")
    args = parser.parse_args()
    report = {
        "status": "passed",
        "exact_count_laws": check_exact_count_identities(),
        "phase_concentration": check_phase_geometry(),
        "finite_probability_diagnostics": check_finite_probabilities(),
        "scope": "Finite identities and selected parameter cases support, but do not prove, the all-parameter theorem.",
    }
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
