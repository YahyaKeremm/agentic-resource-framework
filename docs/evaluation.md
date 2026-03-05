# Evaluation Plan

## Scenarios (synthetic traffic)

- steady load
- burst traffic
- periodic spikes
- drifting demand (non-stationary shift)

## Baselines

1) Static allocation baseline
- equal share or predefined shares per slice

2) Rule-based adaptive controller
- if URLLC delay violation -> INC(URLLC)
- if fairness imbalance -> REBALANCE_FAIR
- else HOLD

## Metrics

Per slice:
- delay D_i
- throughput T_i
- loss L_i
System-level:
- fairness J
- violation rates (per slice and overall)

## Outputs

- time-series plots for metrics and allocations
- summary table per scenario (mean, std, violation rate)
- comparison baseline vs adaptive policy
