# Available Agents

This page lists all 80+ negotiation agents available through the negmas-geniusweb-bridge.

## Naming Convention

- **Raw agents** (GeniusWeb DefaultParty classes): `AgentName` (e.g., `HammingAgent`)
- **Wrapped agents** (NegMAS-compatible): `GWAgentName` (e.g., `GWHammingAgent`)

## Agent Modules

| Module | Count | Type | Description |
|--------|-------|------|-------------|
| `basic` | 7 | Python Native | Reference implementations |
| `anac2020` | 13 | AI-Translated | ANAC 2020 competition (from Java) |
| `anl2022` | 19 | Python Native | ANL 2022 competition |
| `anl2023` | 16 | Python Native | ANL 2023 competition |
| `cse3210` | 25 | Python Native | TU Delft course agents |

---

## Basic Agents (7) - Python Native

Reference implementations of classic negotiation strategies.

| Agent | Wrapped Name | Description |
|-------|--------------|-------------|
| `BoulwareAgent` | `GWBoulwareAgent` | Time-dependent concession (hardliner early, concedes late) |
| `ConcederAgent` | `GWConcederAgent` | Time-dependent concession (concedes early) |
| `LinearAgent` | `GWLinearAgent` | Linear concession over time |
| `HardlinerAgent` | `GWHardlinerAgent` | Never concedes (testing only) |
| `RandomAgent` | `GWRandomAgent` | Random bid selection |
| `StupidAgent` | `GWStupidAgent` | Simple random behavior (test agent) |
| `TimeDependentAgent` | `GWTimeDependentAgent` | Base class with configurable `e` parameter |

---

## ANAC 2020 Agents (13) - AI-Translated from Java

Agents from the Automated Negotiating Agents Competition 2020.

!!! warning "AI-Translated"
    These agents were translated from Java using AI assistance. They may contain differences from the original implementations.

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

---

## ANL 2022 Agents (19) - Python Native

Agents from the Automated Negotiation League 2022.

| Agent | Wrapped Name | Notes |
|-------|--------------|-------|
| `Agent007` | `GWAgent007` | |
| `Agent4410` | `GWAgent4410` | |
| `AgentFish` | `GWAgentFish` | |
| `AgentFO2` | `GWAgentFO2` | |
| `BIU_agent` | `GWBIU_agent` | May timeout >60 secs |
| `ChargingBoul` | `GWChargingBoul` | |
| `CompromisingAgent` | `GWCompromisingAgent` | May cause "Action cannot be None" |
| `DreamTeam109Agent` | `GWDreamTeam109Agent` | |
| `GEAAgent` | `GWGEAAgent` | Slow (~1.5sec per turn) |
| `LearningAgent` | `GWLearningAgent` | May cause "Action cannot be None" |
| `LuckyAgent2022` | `GWLuckyAgent2022` | |
| `MiCROAgent` | `GWMiCROAgent` | |
| `Pinar_Agent` | `GWPinar_Agent` | Requires `lightgbm` (optional) |
| `ProcrastinAgent` | `GWProcrastinAgent` | Issues with first offer |
| `RGAgent` | `GWRGAgent` | |
| `SmartAgent` | `GWSmartAgent` | |
| `SuperAgent` | `GWSuperAgent` | |
| `ThirdAgent` | `GWThirdAgent` | |
| `Tjaronchery10Agent` | `GWTjaronchery10Agent` | |

---

## ANL 2023 Agents (16) - Python Native

Agents from the Automated Negotiation League 2023.

| Agent | Wrapped Name | Notes |
|-------|--------------|-------|
| `AgentFO3` | `GWAgentFO3` | |
| `AmbitiousAgent` | `GWAmbitiousAgent` | |
| `AntAllianceAgent` | `GWAntAllianceAgent` | |
| `AntHeartAgent` | `GWAntHeartAgent` | |
| `ColmanAnacondotAgent2` | `GWColmanAnacondotAgent2` | |
| `ExploitAgent` | `GWExploitAgent` | |
| `GOTAgent` | `GWGOTAgent` | |
| `HybridAgent2023` | `GWHybridAgent2023` | |
| `KBTimeDiffAgent` | `GWKBTimeDiffAgent` | |
| `Micro2023` | `GWMicro2023` | |
| `MSCAgent` | `GWMSCAgent` | Requires `gym`, `torch`, `stable-baselines3` (optional) |
| `PopularAgent` | `GWPopularAgent` | |
| `SmartAgent2023` | `GWSmartAgent2023` | |
| `SpaghettiAgent` | `GWSpaghettiAgent` | |
| `TripleEAgent` | `GWTripleEAgent` | |

---

## CSE3210 Agents (25) - Python Native

Agents from the TU Delft CSE3210 Negotiation course.

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

---

## Usage Examples

### Using a Single Agent

```python
from negmas import SAOMechanism, make_issue
from negmas.preferences import LinearAdditiveUtilityFunction

from negmas_geniusweb_bridge.anac2020 import GWHammingAgent

issues = [make_issue(10, "price"), make_issue(5, "quality")]
ufun = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)

mechanism = SAOMechanism(issues=issues, n_steps=50)
mechanism.add(GWHammingAgent(ufun=ufun, name="agent1"))
# Add another agent...
mechanism.run()
```

### Accessing All Agents from a Module

```python
from negmas_geniusweb_bridge.anac2020 import AGENTS, WRAPPED_AGENTS, AGENT_METADATA
from negmas_geniusweb_bridge.anl2022 import AGENTS, WRAPPED_AGENTS, AGENT_NOTES

# List all available agents
print(list(AGENTS.keys()))  # Raw GeniusWeb agents
print(list(WRAPPED_AGENTS.keys()))  # NegMAS-wrapped agents

# Get metadata about an agent (ANAC 2020 only)
info = AGENT_METADATA["HammingAgent"]
print(info["description"])
print(info["tags"])  # ['AI-translated', 'SAOP']
```

### Creating Custom Wrapped Agents

```python
from negmas_geniusweb_bridge.wrapper import make_geniusweb_negotiator
from negmas_geniusweb_bridge.basic.boulware_agent.boulware_agent import BoulwareAgent

# Create a reusable negotiator class
BoulwareNegotiator = make_geniusweb_negotiator(BoulwareAgent)

# Use it like any other NegMAS negotiator
negotiator = BoulwareNegotiator(ufun=my_ufun, name="boulware1")
```

### Checking Optional Agent Availability

```python
from negmas_geniusweb_bridge.anl2022 import PINAR_AGENT_AVAILABLE, Pinar_Agent
from negmas_geniusweb_bridge.anl2023 import MSC_AGENT_AVAILABLE, MSCAgent

if PINAR_AGENT_AVAILABLE:
    print("Pinar_Agent is available (lightgbm installed)")
else:
    print("Pinar_Agent not available (install lightgbm)")

if MSC_AGENT_AVAILABLE:
    print("MSCAgent is available (gym/torch/stable-baselines3 installed)")
else:
    print("MSCAgent not available")
```
