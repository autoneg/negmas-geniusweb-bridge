# Agents Reference

This page documents all available negotiation agents in the bridge library.

## Importing Agents

All wrapped agents (NegMAS-compatible) are prefixed with `GW` and can be imported directly:

```python
# Import specific wrapped agents
from negmas_geniusweb_bridge import GWBoulwareAgent, GWHammingAgent

# Import all agents as a dictionary
from negmas_geniusweb_bridge import ALL_AGENTS

# Import from specific modules
from negmas_geniusweb_bridge.basic import GWBoulwareAgent, GWConcederAgent
from negmas_geniusweb_bridge.anac2020 import GWHammingAgent, GWShineAgent
from negmas_geniusweb_bridge.anac2021 import GWAgentFO2021, GWAlphaBIU
from negmas_geniusweb_bridge.anl2022 import GWAgent007, GWMiCROAgent
from negmas_geniusweb_bridge.anl2023 import GWAgentFO3, GWPopularAgent
from negmas_geniusweb_bridge.cse3210 import GWAgent11, GWAgent27
```

## Module Structure

Each agent module exports:

- `AGENTS` - Dictionary of raw GeniusWeb party classes
- `WRAPPED_AGENTS` - Dictionary of NegMAS-wrapped negotiator classes
- `AGENT_NOTES` - Known issues/notes about specific agents (where applicable)
- Individual agent classes (both raw and wrapped)

---

## Basic Agents

Reference implementations of common negotiation strategies.

| Agent | Wrapped Name | Description |
|-------|--------------|-------------|
| `BoulwareAgent` | `GWBoulwareAgent` | Time-dependent concession (hardliner early, concedes late) |
| `ConcederAgent` | `GWConcederAgent` | Time-dependent concession (concedes early) |
| `LinearAgent` | `GWLinearAgent` | Linear concession over time |
| `HardlinerAgent` | `GWHardlinerAgent` | Never concedes (testing only) |
| `RandomAgent` | `GWRandomAgent` | Random bid selection |
| `StupidAgent` | `GWStupidAgent` | Simple random behavior (test agent) |
| `TimeDependentAgent` | `GWTimeDependentAgent` | Base class with configurable `e` parameter |

??? info "API Reference - Basic Agents"
    ::: negmas_geniusweb_bridge.basic
        options:
          show_source: false
          members:
            - AGENTS
            - WRAPPED_AGENTS
            - BoulwareAgent
            - ConcederAgent
            - LinearAgent
            - HardlinerAgent
            - RandomAgent
            - StupidAgent
            - TimeDependentAgent

---

## ANAC 2020 Agents

Agents translated from Java implementations submitted to ANAC 2020.

!!! warning "AI-Translated Code"
    These agents were translated from Java to Python using AI assistance.
    While functionally equivalent, they may have subtle differences from the originals.

| Agent | Wrapped Name | Protocol | Description |
|-------|--------------|----------|-------------|
| `AgentKT` | `GWAgentKT` | SHAOP/SAOP | COBYLA optimization with game-theoretic thresholds |
| `AgentP1DAMO` | `GWAgentP1DAMO` | SHAOP | Hill climbing with importance maps |
| `AgentXX` | `GWAgentXX` | SHAOP/SAOP | Importance maps with Nash point estimation |
| `AhBuNeAgent` | `GWAhBuNeAgent` | SHAOP | Similarity-based bidding with elicitation |
| `Anaconda` | `GWAnaconda` | SHAOP | Dynamic lower bounds with elicitation |
| `Angel` | `GWAngel` | SHAOP/SAOP | Heuristic opponent modeling with elicitation |
| `AzarAgent` | `GWAzarAgent` | SHAOP/SAOP | GravityEs user model with frequency modeling |
| `BlingBling` | `GWBlingBling` | SHAOP/SAOP | RankNet neural network for preference learning |
| `DUOAgent` | `GWDUOAgent` | SHAOP/SAOP | Linear regression for bid prediction |
| `ForArisa` | `GWForArisa` | SAOP | Genetic algorithm for utility estimation |
| `HammingAgent` | `GWHammingAgent` | SAOP | Hamming distance for opponent modeling |
| `NiceAgent` | `GWNiceAgent` | SHAOP/SAOP | Elicitation with mirroring strategy |
| `ShineAgent` | `GWShineAgent` | SAOP | Adaptive agent with dynamic strategy |

??? info "API Reference - ANAC 2020 Agents"
    ::: negmas_geniusweb_bridge.anac2020
        options:
          show_source: false
          members:
            - AGENTS
            - WRAPPED_AGENTS
            - AgentKT
            - AgentP1DAMO
            - AgentXX
            - AhBuNeAgent
            - Anaconda
            - Angel
            - AzarAgent
            - BlingBling
            - DUOAgent
            - ForArisa
            - HammingAgent
            - NiceAgent
            - ShineAgent

---

## ANAC 2021 Agents

Agents translated from Java implementations submitted to ANAC 2021.

!!! warning "AI-Translated Code"
    These agents were translated from Java to Python using AI assistance.

| Agent | Wrapped Name | Description |
|-------|--------------|-------------|
| `AgentFO2021` | `GWAgentFO2021` | Learning-based agent with time-dependent concession |
| `AlphaBIU` | `GWAlphaBIU` | Frequency-based opponent modeling with two-phase strategy |
| `GamblerAgent` | `GWGamblerAgent` | UCB Multi-Armed Bandit selecting among sub-agents |
| `MatrixAlienAgent` | `GWMatrixAlienAgent` | Adaptive boulware-style with multi-factor bid scoring |
| `TheDiceHaggler2021` | `GWTheDiceHaggler2021` | Multi-phase strategy with Pareto estimation and TOPSIS |
| `TripleAgent` | `GWTripleAgent` | Frequency model and utility space analysis |

??? info "API Reference - ANAC 2021 Agents"
    ::: negmas_geniusweb_bridge.anac2021
        options:
          show_source: false
          members:
            - AGENTS
            - WRAPPED_AGENTS
            - AgentFO2021
            - AlphaBIU
            - GamblerAgent
            - MatrixAlienAgent
            - TheDiceHaggler2021
            - TripleAgent

---

## ANL 2022 Agents

Native Python agents from the Automated Negotiation League 2022.

| Agent | Wrapped Name | Notes |
|-------|--------------|-------|
| `Agent007` | `GWAgent007` | |
| `Agent4410` | `GWAgent4410` | |
| `AgentFish` | `GWAgentFish` | |
| `AgentFO2` | `GWAgentFO2` | May timeout >60 secs |
| `BIUAgent` | `GWBIUAgent` | May timeout >60 secs |
| `ChargingBoul` | `GWChargingBoul` | |
| `CompromisingAgent` | `GWCompromisingAgent` | May cause "Action cannot be None" |
| `DreamTeam109Agent` | `GWDreamTeam109Agent` | |
| `GEAAgent` | `GWGEAAgent` | Slow (~1.5sec per turn) |
| `LearningAgent` | `GWLearningAgent` | May cause "Action cannot be None" |
| `LuckyAgent2022` | `GWLuckyAgent2022` | |
| `MiCROAgent` | `GWMiCROAgent` | |
| `PinarAgent` | `GWPinarAgent` | Requires `lightgbm` (optional) |
| `ProcrastinAgent` | `GWProcrastinAgent` | Issues with first offer |
| `RGAgent` | `GWRGAgent` | |
| `SmartAgent` | `GWSmartAgent` | |
| `SuperAgent` | `GWSuperAgent` | |
| `ThirdAgent` | `GWThirdAgent` | |
| `Tjaronchery10Agent` | `GWTjaronchery10Agent` | |

??? info "API Reference - ANL 2022 Agents"
    ::: negmas_geniusweb_bridge.anl2022
        options:
          show_source: false
          members:
            - AGENTS
            - WRAPPED_AGENTS
            - AGENT_NOTES

---

## ANL 2023 Agents

Native Python agents from the Automated Negotiation League 2023.

| Agent | Wrapped Name | Notes |
|-------|--------------|-------|
| `AgentFO3` | `GWAgentFO3` | |
| `AmbitiousAgent` | `GWAmbitiousAgent` | |
| `AntAllianceAgent` | `GWAntAllianceAgent` | |
| `AntHeartAgent` | `GWAntHeartAgent` | |
| `ColmanAnacondotAgent2` | `GWColmanAnacondotAgent2` | |
| `ExploitAgent` | `GWExploitAgent` | |
| `GotAgent` | `GWGotAgent` | |
| `HybridAgent2023` | `GWHybridAgent2023` | |
| `KBTimeDiffAgent` | `GWKBTimeDiffAgent` | |
| `MiCRO2023` | `GWMiCRO2023` | |
| `MSCAgent` | `GWMSCAgent` | Requires `gym`, `torch`, `stable-baselines3` (optional) |
| `PopularAgent` | `GWPopularAgent` | |
| `SmartAgent` | `GWSmartAgent` | |
| `SpaghettiAgent` | `GWSpaghettiAgent` | |
| `TripleEAgent` | `GWTripleEAgent` | |

??? info "API Reference - ANL 2023 Agents"
    ::: negmas_geniusweb_bridge.anl2023
        options:
          show_source: false
          members:
            - AGENTS
            - WRAPPED_AGENTS

---

## CSE3210 Agents

Agents from the TU Delft CSE3210 Negotiation course (25 agents).

| Agent | Wrapped Name | Notes |
|-------|--------------|-------|
| `Agent2` | `GWAgent2` | |
| `Agent3` | `GWAgent3` | |
| `Agent7` | `GWAgent7` | |
| `Agent11` | `GWAgent11` | |
| `Agent14` | `GWAgent14` | |
| `Agent18` | `GWAgent18` | |
| `Agent19` | `GWAgent19` | |
| `Agent22` | `GWAgent22` | May throw scipy divide by zero |
| `Agent24` | `GWAgent24` | |
| `Agent25` | `GWAgent25` | |
| `Agent26` | `GWAgent26` | |
| `Agent27` | `GWAgent27` | |
| `Agent29` | `GWAgent29` | |
| `Agent32` | `GWAgent32` | |
| `Agent33` | `GWAgent33` | |
| `Agent41` | `GWAgent41` | |
| `Agent43` | `GWAgent43` | |
| `Agent50` | `GWAgent50` | |
| `Agent52` | `GWAgent52` | |
| `Agent55` | `GWAgent55` | |
| `Agent58` | `GWAgent58` | |
| `Agent61` | `GWAgent61` | |
| `Agent64` | `GWAgent64` | |
| `Agent67` | `GWAgent67` | |
| `Agent68` | `GWAgent68` | Issues with opening bid |

??? info "API Reference - CSE3210 Agents"
    ::: negmas_geniusweb_bridge.cse3210
        options:
          show_source: false
          members:
            - AGENTS
            - WRAPPED_AGENTS
            - AGENT_NOTES

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

All agents support:

- **Protocol**: SAOP (Stacked Alternating Offers Protocol)
- **Profile Types**: LinearAdditive utility functions

## Agent Dictionaries

Access all agents programmatically:

```python
from negmas_geniusweb_bridge import ALL_AGENTS, TRAINING_AGENTS, TESTING_AGENTS

# ALL_AGENTS contains all 82 wrapped agents
print(f"Total agents: {len(ALL_AGENTS)}")

# Access by name
agent_class = ALL_AGENTS["GWBoulwareAgent"]
negotiator = agent_class(name="boulware")

# List all available agents
for name in sorted(ALL_AGENTS.keys()):
    print(name)
```

??? info "API Reference - Main Module Dictionaries"
    ::: negmas_geniusweb_bridge
        options:
          show_source: false
          members:
            - ALL_AGENTS
            - TRAINING_AGENTS
            - TESTING_AGENTS
            - GENIUS_WEB_AVAILABLE
            - REGISTRY_AVAILABLE
