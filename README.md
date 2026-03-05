# agentic-resource-framework

An agentic (LLM) adaptive resource management framework for 5G network slicing, built around:
- synthetic non-stationary traffic generation
- a lightweight analytical (abstracted) network environment
- symbolic state abstraction
- an agentic decision module that outputs discrete high-level actions
- a deterministic adapter that applies actions as constrained allocation updates
- evaluation with QoS metrics (delay, throughput, loss, fairness)

This is **not** a full 5G simulator. The environment is intentionally abstracted and analytical to maximize iteration speed and experimental control.

## Core Idea

At each discrete timestep `t`, we have:
- demand vector: `d(t)` for `N` slices
- allocation vector: `a(t)` where `sum(a) = 1` and `a_i >= a_min`
- environment computes QoS metrics `m(t)` from `(a(t), d(t))`
- symbolic abstraction encodes `(m(t), a(t), d(t)) -> s(t)`
- agent selects a discrete action `u(t)` based on `s(t)`
- adapter updates allocation incrementally: `a(t+1) = Projection(a(t) + Δa(u(t)))`

We follow **incremental control (B-model)**:
- the agent does **not** output the full allocation directly
- the agent outputs **an action** that implies a bounded update step (e.g., +5% to slice k)

## Default Slice Setup

We start with `N = 3` canonical slices:
- eMBB: throughput-oriented
- URLLC: latency-critical
- mMTC: massive IoT / delay-tolerant

Each slice can have different QoS targets (slice-specific delay thresholds).

## Repository Structure
- TBD

## Planned Milestones

**Step 1**
- Environment model v0 (queueing-inspired analytical mapping)
- Symbolic abstraction v0 (LOW/MED/HIGH load, delay violations, fairness state)
- Action space + adapter with constrained projection
- End-to-end runner that logs metrics and produces baseline plots

**Step 2**
- Experiment runner over multiple traffic scenarios
- Baselines: static allocation + rule-based adaptive policy
- Unit tests for projection, environment sanity, abstraction edges
- Clean modular interfaces (agent slot ready for LLM decision module)

  ## Quick Start (placeholder)

  1. Create a virtual environment
  2. Install dependencies
  3. Run the demo experiment
 
  (Will be filled after the first runnable pipeline is committed.)
