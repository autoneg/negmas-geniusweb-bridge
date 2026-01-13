# Agents Reference

This page documents all available negotiation agents in the bridge library.

## Basic Agents

Basic reference implementations for negotiation agents.

### RandomAgent
::: negmas_geniusweb_bridge.basic.random_agent.random_agent.RandomAgent

### LinearAgent
::: negmas_geniusweb_bridge.basic.linear_agent.linear_agent.LinearAgent

### BoulwareAgent
::: negmas_geniusweb_bridge.basic.boulware_agent.boulware_agent.BoulwareAgent

### ConcederAgent
::: negmas_geniusweb_bridge.basic.conceder_agent.conceder_agent.ConcederAgent

### HardlinerAgent
::: negmas_geniusweb_bridge.basic.hardliner_agent.hardliner_agent.HardlinerAgent

### TimeDependentAgent
::: negmas_geniusweb_bridge.basic.time_dependent_agent.time_dependent_agent.TimeDependentAgent

---

## ANAC 2020 Agents

Agents translated from Java implementations submitted to ANAC 2020.

!!! warning "AI-Translated Code"
    These agents were translated from Java to Python using AI assistance.
    While functionally equivalent, they may have subtle differences from the originals.

### HammingAgent
::: negmas_geniusweb_bridge.anac2020.hamming_agent.hamming_agent.HammingAgent

### ShineAgent
::: negmas_geniusweb_bridge.anac2020.shine_agent.shine_agent.ShineAgent

### DUOAgent
::: negmas_geniusweb_bridge.anac2020.duo_agent.duo_agent.DUOAgent

---

## ANL 2022 Agents

Native Python agents from the Automated Negotiation League 2022.

These agents are native Python implementations and do not require translation.

See the source code in `src/negmas_geniusweb_bridge/anl2022/` for available agents.

---

## ANL 2023 Agents

Native Python agents from the Automated Negotiation League 2023.

See the source code in `src/negmas_geniusweb_bridge/anl2023/` for available agents.

---

## CSE3210 Agents

Agents from the TU Delft CSE3210 course.

See the source code in `src/negmas_geniusweb_bridge/cse3210/` for available agents.

---

## Using Wrapped Agents

All agents are available in two forms:

1. **Raw GeniusWeb agents** - Extend `DefaultParty`, for use with GeniusWeb infrastructure
2. **Wrapped negotiators** - Prefixed with `GW`, for use with NegMAS mechanisms

```python
# Import wrapped agents directly
from negmas_geniusweb_bridge import GWHammingAgent, GWShineAgent

# Or import raw agents
from negmas_geniusweb_bridge.anac2020 import HammingAgent, ShineAgent

# Create wrapped negotiators
negotiator = GWHammingAgent(name="hamming")
```

## Agent Capabilities

Each agent declares its capabilities:

| Agent | Protocols | Profile Types |
|-------|-----------|---------------|
| HammingAgent | SAOP | LinearAdditive |
| ShineAgent | SAOP | LinearAdditive |
| DUOAgent | SAOP | LinearAdditive |
| RandomAgent | SAOP | LinearAdditive |
| LinearAgent | SAOP | LinearAdditive |
