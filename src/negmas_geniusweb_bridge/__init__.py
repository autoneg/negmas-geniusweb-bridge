"""
NegMAS-GeniusWeb Bridge.

This module provides wrapped GeniusWeb negotiation agents that can be used
with NegMAS mechanisms. All wrapped classes are prefixed with "GW" to avoid
name clashes with the unwrapped GeniusWeb party classes.

Example:
    >>> from negmas_geniusweb_bridge import GWBoulwareAgent
    >>> negotiator = GWBoulwareAgent(ufun=my_ufun)
"""

from typing import Any

from .wrapper import (
    make_geniusweb_negotiator as make_negotiator,
    GeniusWebNegotiator,
    GENIUS_WEB_AVAILABLE,
)

# Import agent dictionaries from each module
from .anl2022 import AGENTS as ANL2022_AGENTS
from .anl2023 import AGENTS as ANL2023_AGENTS
from .basic import AGENTS as BASIC_AGENTS
from .cse3210 import AGENTS as CSE3210_AGENTS
from .anac2020 import AGENTS as ANAC2020_AGENTS, WRAPPED_AGENTS as ANAC2020_WRAPPED
from .anac2021 import AGENTS as ANAC2021_AGENTS, WRAPPED_AGENTS as ANAC2021_WRAPPED
from .ai2020 import AGENTS as AI2020_AGENTS, WRAPPED_AGENTS as AI2020_WRAPPED

# Import individual wrapped classes for direct use
from .anac2020 import GWHammingAgent, GWShineAgent

# Dictionaries for agent management
TRAINING_AGENTS: dict[str, Any] = {}
TESTING_AGENTS: dict[str, Any] = {}
ALL_AGENTS: dict[str, Any] = {}

# Add wrapped agents from each source
# Native Python agents (ANL2022, ANL2023, CSE3210, BASIC)
ALL_AGENTS.update({f"GW{k}": make_negotiator(v) for k, v in ANL2022_AGENTS.items()})
ALL_AGENTS.update({f"GW{k}": make_negotiator(v) for k, v in ANL2023_AGENTS.items()})
ALL_AGENTS.update({f"GW{k}": make_negotiator(v) for k, v in BASIC_AGENTS.items()})
ALL_AGENTS.update({f"GW{k}": make_negotiator(v) for k, v in CSE3210_AGENTS.items()})

# AI-translated agents (ANAC2020, ANAC2021, AI2020)
ALL_AGENTS.update(ANAC2020_WRAPPED)
ALL_AGENTS.update(ANAC2021_WRAPPED)
ALL_AGENTS.update(AI2020_WRAPPED)

TRAINING_AGENTS = ALL_AGENTS.copy()
TESTING_AGENTS = ALL_AGENTS.copy()

__all__ = [
    # Core classes
    "GeniusWebNegotiator",
    "make_negotiator",
    "GENIUS_WEB_AVAILABLE",
    # Agent dictionaries
    "ALL_AGENTS",
    "TRAINING_AGENTS",
    "TESTING_AGENTS",
    # Individual wrapped agents (ANAC2020 - AI translated)
    "GWHammingAgent",
    "GWShineAgent",
    # Raw agent dictionaries (for advanced users)
    "ANL2022_AGENTS",
    "ANL2023_AGENTS",
    "BASIC_AGENTS",
    "CSE3210_AGENTS",
    "ANAC2020_AGENTS",
    "ANAC2021_AGENTS",
    "AI2020_AGENTS",
]
