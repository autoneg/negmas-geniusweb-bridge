# negmas-geniusweb-bridge

A bridge that allows you to run [GeniusWeb](https://tracinsy.ewi.tudelft.nl/pubtrac/GeniusWeb) negotiation agents within [NegMAS](https://github.com/yasserfarouk/negmas) mechanisms.

## Official GeniusWeb Resources

This project builds upon the official GeniusWeb framework. For the original implementations:

- **GeniusWeb (Java)**: [https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniusweb](https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniusweb)
- **GeniusWeb (Python)**: [https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniuswebpython](https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniuswebpython)
- **GeniusWeb Project Home**: [https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb](https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb)

The official repositories contain:
- Complete GeniusWeb framework implementation (Java and Python)
- Competition agents from ANAC 2020-2022
- Documentation and examples

## AI-Assisted Development Disclaimer

**Important Notice**: Parts of this project were developed with AI assistance:

- **GeniusWeb-to-NegMAS Wrapper** (`wrapper.py`): The bridge wrapper that enables GeniusWeb agents to run in NegMAS mechanisms was developed in part using AI assistance.
- **Java-to-Python Translations**: The negotiation agents in the `anac2020/`, `anac2021/`, and `ai2020/` directories were translated from their original Java implementations to Python using AI. These translations aim to preserve the original algorithms and strategies but may contain differences from the original implementations.

The original Python agents (in `basic/`, `anl2022/`, `anl2023/`, `cse3210/`) were written directly in Python by their original authors and are not AI-translated.

Users should be aware that AI-translated code may require additional validation for research or production use.

## Installation

```bash
uv sync
```

For local development with a local negmas installation:
```bash
uv sync && uv pip install -e ../negmas
```

## Usage

### Basic Example

Run a negotiation between a GeniusWeb agent and a NegMAS agent:

```python
from negmas import SAOMechanism, make_issue
from negmas.preferences import LinearAdditiveUtilityFunction
from negmas.sao import AspirationNegotiator

from negmas_geniusweb_bridge.wrapper import GeniusWebNegotiator
from negmas_geniusweb_bridge.basic.boulware_agent.boulware_agent import BoulwareAgent

# Define the negotiation issues
issues = [make_issue(5, "price"), make_issue(3, "quality")]

# Create utility functions for each agent
ufun_a = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)
ufun_b = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)

# Create the negotiation mechanism
mechanism = SAOMechanism(issues=issues, n_steps=50)

# Create a GeniusWeb agent (Boulware strategy)
gw_agent = GeniusWebNegotiator(
    party_class=BoulwareAgent,
    ufun=ufun_a,
    name="geniusweb_boulware",
)

# Create a NegMAS agent (Aspiration strategy)
negmas_agent = AspirationNegotiator(ufun=ufun_b, name="aspiration")

# Add agents to the mechanism
mechanism.add(gw_agent)
mechanism.add(negmas_agent)

# Run the negotiation
mechanism.run()

# Check results
state = mechanism.state
print(f"Agreement: {state.agreement}")
print(f"Steps: {state.step}")
```

### GeniusWeb vs GeniusWeb

Run a negotiation between two GeniusWeb agents:

```python
from negmas import SAOMechanism, make_issue
from negmas.preferences import LinearAdditiveUtilityFunction

from negmas_geniusweb_bridge.wrapper import GeniusWebNegotiator
from negmas_geniusweb_bridge.basic.boulware_agent.boulware_agent import BoulwareAgent
from negmas_geniusweb_bridge.basic.conceder_agent.conceder_agent import ConcederAgent

issues = [make_issue(10, "price"), make_issue(5, "quality"), make_issue(3, "delivery")]

ufun_a = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)
ufun_b = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)

mechanism = SAOMechanism(issues=issues, n_steps=100)

# Boulware agent (reluctant to concede)
agent_a = GeniusWebNegotiator(
    party_class=BoulwareAgent,
    ufun=ufun_a,
    name="boulware",
)

# Conceder agent (willing to concede quickly)
agent_b = GeniusWebNegotiator(
    party_class=ConcederAgent,
    ufun=ufun_b,
    name="conceder",
)

mechanism.add(agent_a)
mechanism.add(agent_b)
mechanism.run()

print(f"Agreement: {mechanism.state.agreement}")
```

### Using the Factory Function

Create reusable negotiator classes:

```python
from negmas_geniusweb_bridge.wrapper import make_geniusweb_negotiator
from negmas_geniusweb_bridge.basic.boulware_agent.boulware_agent import BoulwareAgent

# Create a reusable negotiator class
BoulwareNegotiator = make_geniusweb_negotiator(BoulwareAgent)

# Use it like any other NegMAS negotiator
negotiator = BoulwareNegotiator(ufun=my_ufun, name="boulware1")
```

## Available Agents

The bridge includes agents from several GeniusWeb competitions:

### Native Python Agents
- **Basic agents**: `BoulwareAgent`, `ConcederAgent`, `LinearAgent`, `HardlinerAgent`, `RandomAgent`
- **ANL2022**: Competition agents from the Automated Negotiating Agents Competition 2022
- **ANL2023**: Competition agents from ANL 2023
- **CSE3210**: Educational agents from TU Delft course

### AI-Translated Agents (from Java)
- **ANAC2020**: Agents from ANAC 2020 competition (AI-translated from Java)
- **ANAC2021**: Agents from ANAC 2021 competition (AI-translated from Java)
- **AI2020**: Agents from AI course 2020 (AI-translated from Java)

## Testing

```bash
# Run all tests
uv run pytest

# Run a specific test
uv run pytest tests/test_negmas_wrapper.py::TestNegotiationRuns::test_geniusweb_vs_geniusweb -v
```

## License

This software is licensed for **academic, research, and non-commercial use only**.

Commercial use requires a separate license. Contact the author for commercial licensing inquiries.

See [LICENSE](LICENSE) for full terms.
