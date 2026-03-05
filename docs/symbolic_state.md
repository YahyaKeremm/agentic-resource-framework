# Symbolic State Abstraction

## Motivation

Symbolic abstraction reduces complexity and makes the system LLM-friendly:
- avoids high-dimensional continuous states
- creates interpretable decisions (HIGH load, delay violation, fairness imbalance)

## Symbols (v0)

For each slice i:

1) Load level from utilization ρ_i:
- LOW: ρ < 0.60
- MED: 0.60 <= ρ < 0.85
- HIGH: ρ >= 0.85

2) Delay violation:
- TRUE if D_i > D_target_i else FALSE

System-level:

3) Fairness state from Jain index J:
- OK if J >= J_threshold
- IMBALANCED if J < J_threshold

## Example Symbolic State

- load_levels: [MED, HIGH, LOW]
- delay_violations: [False, True, False]
- fairness: IMBALANCED

Threshold values are stored in `TBD`.
