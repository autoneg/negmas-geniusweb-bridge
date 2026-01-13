# negmas-geniusweb-bridge

A bridge that allows you to run GeniusWeb negotiation agents in NegMAS SAOMechanism(s).

## Overview

This library provides a seamless way to use negotiation agents originally developed for the [GeniusWeb](https://tracinsy.ewi.tudelft.nl/pubtrac/GeniusWeb) platform within [NegMAS](https://negmas.readthedocs.io/) (Negotiation Agents, Mechanisms, and Simulations).

## Official GeniusWeb Resources

This project builds upon the official GeniusWeb framework. For the original implementations:

- **GeniusWeb (Java)**: [https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniusweb](https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniusweb)
- **GeniusWeb (Python)**: [https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniuswebpython](https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb/geniuswebpython)
- **GeniusWeb Project Home**: [https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb](https://gitlab.ewi.tudelft.nl/interactive-intelligence/geniusweb)

The official repositories contain the complete GeniusWeb framework implementation (Java and Python), competition agents from ANAC 2020-2022, and documentation.

## Features

- Run GeniusWeb agents in NegMAS negotiation mechanisms
- Mix GeniusWeb and native NegMAS agents in the same negotiation
- Use agents from ANAC competitions (2020, 2021, 2022, 2023)
- Access to numerous pre-implemented negotiation strategies

## Quick Start

```python
from negmas import SAOMechanism, make_issue, make_os
from negmas_geniusweb_bridge import GWHammingAgent

# Create a negotiation scenario
issues = [make_issue(name="price", values=10), make_issue(name="quantity", values=5)]
mechanism = SAOMechanism(outcome_space=make_os(issues), n_steps=100)

# Add a wrapped GeniusWeb agent
mechanism.add(GWHammingAgent(name="gw_agent"))

# Run the negotiation
mechanism.run()
```

## Installation

```bash
pip install negmas-geniusweb-bridge
```

Or with uv:

```bash
uv add negmas-geniusweb-bridge
```

## Documentation

- [Getting Started](getting-started/installation.md) - Installation and setup
- [User Guide](user-guide/agents.md) - Available agents and usage patterns
- [API Reference](api/wrappers.md) - Detailed API documentation
- [Development](development/contributing.md) - Contributing guidelines

## License

MIT License - see [LICENSE](https://github.com/yasserfarouk/negmas-geniusweb-bridge/blob/main/LICENSE) for details.
