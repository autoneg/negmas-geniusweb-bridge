# Available Agents

This page lists all the negotiation agents available through the negmas-geniusweb-bridge.

## Naming Convention

- **Raw agents** (GeniusWeb DefaultParty classes): `AgentName` (e.g., `HammingAgent`)
- **Wrapped agents** (NegMAS-compatible): `GWAgentName` (e.g., `GWHammingAgent`)

## ANAC 2020 Agents

Agents from the Automated Negotiating Agents Competition 2020.

| Agent | Wrapped Name | Description | Status |
|-------|--------------|-------------|--------|
| HammingAgent | `GWHammingAgent` | Uses Hamming distance for bid evaluation | Available |
| ShineAgent | `GWShineAgent` | Adaptive bidding with opponent modeling | Available |
| DUOAgent | `GWDUOAgent` | Linear regression-based bid prediction | Available |

## ANL 2022 Agents

Agents from the Automated Negotiation League 2022.

| Agent | Description | Status |
|-------|-------------|--------|
| Agent007 | Strategic negotiation agent | Available |
| AgentFish | Learning-based agent | Available |
| CompromiseAgent | Compromise-seeking strategy | Available |
| ... | ... | ... |

## ANL 2023 Agents

Agents from the Automated Negotiation League 2023.

| Agent | Description | Status |
|-------|-------------|--------|
| ExploitAgent | Exploitation strategy | Available |

## Basic Agents

Reference implementations of classic negotiation strategies.

| Agent | Description |
|-------|-------------|
| BoulwareAgent | Time-dependent concession (hardliner early) |
| ConcederAgent | Time-dependent concession (concedes early) |
| LinearAgent | Linear concession over time |
| HardlinerAgent | Never concedes |
| RandomAgent | Random bid selection |

## Usage Example

```python
from negmas_geniusweb_bridge import GWHammingAgent, GWShineAgent

# Use in a NegMAS mechanism
from negmas import SAOMechanism, make_issue, make_os

issues = [make_issue(name="x", values=10)]
mechanism = SAOMechanism(outcome_space=make_os(issues), n_steps=50)

mechanism.add(GWHammingAgent(name="agent1"))
mechanism.add(GWShineAgent(name="agent2"))

mechanism.run()
```

## Accessing All Agents

You can access agent dictionaries programmatically:

```python
from negmas_geniusweb_bridge.anac2020 import AGENTS, WRAPPED_AGENTS

# List all available agents
print(AGENTS.keys())  # Raw GeniusWeb agents
print(WRAPPED_AGENTS.keys())  # NegMAS-wrapped agents
```
