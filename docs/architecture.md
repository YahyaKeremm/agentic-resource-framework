# System Architecture

## Components

1) Synthetic Traffic Generator
- Produces non-stationary demand traces for each slice:
  - steady load
  - burst events
  - periodic spikes
  - gradual drift / shifting load
 
Output per timestep:
- demand vector `d(t) = [d_1(t), ..., d_N(t)]`

2) Abstracted Network Environment
A lightweight analytical model mapping:
- inputs: allocation `a(t)` and demand `d(t)`
- outputs: QoS metrics `m(t)` for eachs slice:
  - delay
  - throughput
  - packet loss
  - fairness (system-level)

3) Symbolic State Abstraction Layer
Converts raw numerical metrics into a compact symbolic state:
- load level per slice: LOW / MED / HIGH (typically from utilization p)
- delay violation per slice: TRUE / FALSE (D_i > D_target_i)
- fairness state: OK / IMBALANCED (e.g., Jain index < threshold)

4) Agentic Decision Module (LLM-friendly)
Receives symbolic state `s(t)` and selects a discrete action `u(t)` from a bounded action space.

The architecture is model-agnostic:
- can be a rule-based controller
- can be an LLM via API prompting
- can be any other decision module

5) Resource Adaptation Adapter (Deterministic)
Transforms action `u(t)` into a numerical allocation update:
- applies bounded step size δ (e.g., 0.05)
- enforces constraints: `a_i >= a_min`, `sum(a) = 1`
- performs projection back to the feasible simplex

## Data Flow (per timestep)

d(t) -> Environment(a(t), d(t)) -> metrics m(t)
m(t), a(t), d(t) -> Abstraction -> symbolic state s(t)
s(t) -> Agent -> action u(t)
u(t), a(t) -> Adapter/Projection -> a(t+1)
log: {a(t), d(t), m(t), s(t), u(t)}

## Key Design Choice: Incremental Control (B-model)

We use:
- a(t+1) = Projection(a(t) + Δa(u(t)))

instead of:
- a(t) = Agent(s(t))

Benefits:
- more realistic and stable control
- bounded adjustments reduce oscillations
- deterministic adapter separates "decision" from "execution"
