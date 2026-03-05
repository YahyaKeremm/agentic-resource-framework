# Environment Model (Analytical, Queueing-Inspired)

## Purpose

We want a fast, defensible analytical environment (not full simulation) that produces QoS metrics from:
- slice allocation `a(t)`
- slice demand `d(t)`

## Variables

- N: number of slices (default N=3)
- total capacity: C (default constant for initial experiments)
- allocation vector: a(t) where sum(a) = 1
- per-slice service capacity: μ_i(t) = C * a_i(t)
- per-slice arrival/demand: λ_i(t) = d_i(t) (scaled to same units as μ)


## Utilization

ρ_i(t) = λ_i(t) / (μ_i(t) + ε)

## Throughput

T_i(t) = min(λ_i(t), μ_i(t))

## Delay (M/M/1-inspired)

If λ_i < μ_i:
  D_i(t) = 1 / (μ_i(t) - λ_i(t) + ε)

If λ_i >= μ_i:
  The system is unstable; delay can be trated as large / capped, and loss increases.

## Loss (simple approximation)

L_i(t) = max(0, ρ_i(t) - 1)

## Fairness (system-level)

Jain's index over throughputs:
J(t) = ( (sum_i T_i(t))^2 ) / ( N * sum_i (T_i(t)^2) + ε )

## Slice-Specific QoS Targets

Each slice can define a delay target:
D_target = [D_eMBB, D_URLLC, D_mMTC]

Delay violation per slice:
violation_i(t) = (D_i(t) > D_target_i)
