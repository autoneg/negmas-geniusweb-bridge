"""
ANAC 2020 Agents - AI-translated from Java.

These agents were originally implemented in Java for the ANAC 2020 competition
and have been translated to Python using AI assistance.

Exports both raw GeniusWeb party classes and GW-prefixed wrapped negotiators.

Agent Tags:
- "AI-translated": Agent was translated from Java using AI
- "SHAOP": Agent supports/requires SHAOP protocol (preference elicitation via comparisons)
- "SAOP": Agent supports standard SAOP protocol
"""

from typing import Any

from ..wrapper import make_geniusweb_negotiator

# Import raw agents
from .duo_agent.duo_agent import DUOAgent
from .hamming_agent.hamming_agent import HammingAgent
from .shine_agent.shine_agent import ShineAgent

# Dictionary of raw GeniusWeb party classes
AGENTS: dict[str, Any] = {
    "DUOAgent": DUOAgent,
    "HammingAgent": HammingAgent,
    "ShineAgent": ShineAgent,
}

# Agent metadata with tags
# Tags: AI-translated, SHAOP, SAOP, etc.
AGENT_METADATA: dict[str, dict[str, Any]] = {
    "DUOAgent": {
        "class": DUOAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses linear regression for bid prediction with preference elicitation",
    },
    "HammingAgent": {
        "class": HammingAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Uses Hamming distance for opponent modeling",
    },
    "ShineAgent": {
        "class": ShineAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Adaptive agent with dynamic strategy adjustment",
    },
}

# Create GW-prefixed wrapped negotiator classes
GWDUOAgent = make_geniusweb_negotiator(DUOAgent)
GWHammingAgent = make_geniusweb_negotiator(HammingAgent)
GWShineAgent = make_geniusweb_negotiator(ShineAgent)

# Dictionary of wrapped negotiator classes (for registration)
WRAPPED_AGENTS: dict[str, Any] = {
    "GWDUOAgent": GWDUOAgent,
    "GWHammingAgent": GWHammingAgent,
    "GWShineAgent": GWShineAgent,
}

# Wrapped agent metadata (same tags as raw agents)
WRAPPED_AGENT_METADATA: dict[str, dict[str, Any]] = {
    "GWDUOAgent": {
        "class": GWDUOAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses linear regression for bid prediction with preference elicitation",
    },
    "GWHammingAgent": {
        "class": GWHammingAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Uses Hamming distance for opponent modeling",
    },
    "GWShineAgent": {
        "class": GWShineAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Adaptive agent with dynamic strategy adjustment",
    },
}

__all__ = [
    # Raw agents
    "DUOAgent",
    "HammingAgent",
    "ShineAgent",
    # Wrapped agents
    "GWDUOAgent",
    "GWHammingAgent",
    "GWShineAgent",
    # Dictionaries
    "AGENTS",
    "WRAPPED_AGENTS",
    # Metadata
    "AGENT_METADATA",
    "WRAPPED_AGENT_METADATA",
]
