# Action Space and Incremental Updates

## Incremental Control

The agent outputs a discrete action u(t), which the adapter converts into a bounded allocation update:

a(t+1) = Projection(a(t) + Δa(u(t)))

## Discrete Actions (v0)

- HOLD: no change
- INC(k): increase allocation of slice k by δ
- DEC(k): decrease allocation of slice k by δ
- REBALANCE_FAIR: move allocation toward equal shares (or toward a fairness target)

## Step Size

δ is a small constant (e.g., 0.05) defined in config.

## Constraints

- a_i >= a_min
- sum(a) = 1

The adapter enforces constraints via projection onto the feasible simplex.
