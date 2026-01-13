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
from .agent_kt.agent_kt import AgentKT
from .agent_p1_damo.agent_p1_damo import AgentP1DAMO
from .agent_xx.agent_xx import AgentXX
from .ahbune_agent.ahbune_agent import AhBuNeAgent
from .anaconda.anaconda import Anaconda
from .angel.angel import Angel
from .azar_agent.azar_agent import AzarAgent
from .bling_bling.bling_bling import BlingBling
from .duo_agent.duo_agent import DUOAgent
from .for_arisa.for_arisa import ForArisa
from .hamming_agent.hamming_agent import HammingAgent
from .nice_agent.nice_agent import NiceAgent
from .shine_agent.shine_agent import ShineAgent

# Dictionary of raw GeniusWeb party classes
AGENTS: dict[str, Any] = {
    "AgentKT": AgentKT,
    "AgentP1DAMO": AgentP1DAMO,
    "AgentXX": AgentXX,
    "AhBuNeAgent": AhBuNeAgent,
    "Anaconda": Anaconda,
    "Angel": Angel,
    "AzarAgent": AzarAgent,
    "BlingBling": BlingBling,
    "DUOAgent": DUOAgent,
    "ForArisa": ForArisa,
    "HammingAgent": HammingAgent,
    "NiceAgent": NiceAgent,
    "ShineAgent": ShineAgent,
}

# Agent metadata with tags
# Tags: AI-translated, SHAOP, SAOP, etc.
AGENT_METADATA: dict[str, dict[str, Any]] = {
    "AgentKT": {
        "class": AgentKT,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses COBYLA optimization for utility learning with game-theoretic acceptance thresholds",
    },
    "AgentP1DAMO": {
        "class": AgentP1DAMO,
        "tags": ["AI-translated", "SHAOP"],
        "description": "Uses hill climbing optimization with importance maps and time-dependent concession",
    },
    "AgentXX": {
        "class": AgentXX,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses importance maps with Nash point estimation and frequency-based opponent modeling",
    },
    "AhBuNeAgent": {
        "class": AhBuNeAgent,
        "tags": ["AI-translated", "SHAOP"],
        "description": "Uses similarity-based bidding with preference elicitation",
    },
    "Anaconda": {
        "class": Anaconda,
        "tags": ["AI-translated", "SHAOP"],
        "description": "Uses importance maps with dynamic lower bounds and elicitation for SHAOP",
    },
    "Angel": {
        "class": Angel,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses heuristic-based opponent modeling with confidence-scaled elicitation",
    },
    "AzarAgent": {
        "class": AzarAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses GravityEs user model with frequency-based opponent modeling",
    },
    "BlingBling": {
        "class": BlingBling,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses RankNet neural network for preference learning with frequency-based opponent modeling",
    },
    "DUOAgent": {
        "class": DUOAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses linear regression for bid prediction with preference elicitation",
    },
    "ForArisa": {
        "class": ForArisa,
        "tags": ["AI-translated", "SAOP"],
        "description": "Uses genetic algorithm for utility estimation with JohnnyBlack opponent modeling",
    },
    "HammingAgent": {
        "class": HammingAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Uses Hamming distance for opponent modeling",
    },
    "NiceAgent": {
        "class": NiceAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses elicitation to learn preferences and mirroring strategy for offers",
    },
    "ShineAgent": {
        "class": ShineAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Adaptive agent with dynamic strategy adjustment",
    },
}

# Create GW-prefixed wrapped negotiator classes
GWAgentKT = make_geniusweb_negotiator(AgentKT)
GWAgentP1DAMO = make_geniusweb_negotiator(AgentP1DAMO)
GWAgentXX = make_geniusweb_negotiator(AgentXX)
GWAhBuNeAgent = make_geniusweb_negotiator(AhBuNeAgent)
GWAnaconda = make_geniusweb_negotiator(Anaconda)
GWAngel = make_geniusweb_negotiator(Angel)
GWAzarAgent = make_geniusweb_negotiator(AzarAgent)
GWBlingBling = make_geniusweb_negotiator(BlingBling)
GWDUOAgent = make_geniusweb_negotiator(DUOAgent)
GWForArisa = make_geniusweb_negotiator(ForArisa)
GWHammingAgent = make_geniusweb_negotiator(HammingAgent)
GWNiceAgent = make_geniusweb_negotiator(NiceAgent)
GWShineAgent = make_geniusweb_negotiator(ShineAgent)

# Dictionary of wrapped negotiator classes (for registration)
WRAPPED_AGENTS: dict[str, Any] = {
    "GWAgentKT": GWAgentKT,
    "GWAgentP1DAMO": GWAgentP1DAMO,
    "GWAgentXX": GWAgentXX,
    "GWAhBuNeAgent": GWAhBuNeAgent,
    "GWAnaconda": GWAnaconda,
    "GWAngel": GWAngel,
    "GWAzarAgent": GWAzarAgent,
    "GWBlingBling": GWBlingBling,
    "GWDUOAgent": GWDUOAgent,
    "GWForArisa": GWForArisa,
    "GWHammingAgent": GWHammingAgent,
    "GWNiceAgent": GWNiceAgent,
    "GWShineAgent": GWShineAgent,
}

# Wrapped agent metadata (same tags as raw agents)
WRAPPED_AGENT_METADATA: dict[str, dict[str, Any]] = {
    "GWAgentKT": {
        "class": GWAgentKT,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses COBYLA optimization for utility learning with game-theoretic acceptance thresholds",
    },
    "GWAgentP1DAMO": {
        "class": GWAgentP1DAMO,
        "tags": ["AI-translated", "SHAOP"],
        "description": "Uses hill climbing optimization with importance maps and time-dependent concession",
    },
    "GWAgentXX": {
        "class": GWAgentXX,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses importance maps with Nash point estimation and frequency-based opponent modeling",
    },
    "GWAhBuNeAgent": {
        "class": GWAhBuNeAgent,
        "tags": ["AI-translated", "SHAOP"],
        "description": "Uses similarity-based bidding with preference elicitation",
    },
    "GWAnaconda": {
        "class": GWAnaconda,
        "tags": ["AI-translated", "SHAOP"],
        "description": "Uses importance maps with dynamic lower bounds and elicitation for SHAOP",
    },
    "GWAngel": {
        "class": GWAngel,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses heuristic-based opponent modeling with confidence-scaled elicitation",
    },
    "GWAzarAgent": {
        "class": GWAzarAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses GravityEs user model with frequency-based opponent modeling",
    },
    "GWBlingBling": {
        "class": GWBlingBling,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses RankNet neural network for preference learning with frequency-based opponent modeling",
    },
    "GWDUOAgent": {
        "class": GWDUOAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses linear regression for bid prediction with preference elicitation",
    },
    "GWForArisa": {
        "class": GWForArisa,
        "tags": ["AI-translated", "SAOP"],
        "description": "Uses genetic algorithm for utility estimation with JohnnyBlack opponent modeling",
    },
    "GWHammingAgent": {
        "class": GWHammingAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Uses Hamming distance for opponent modeling",
    },
    "GWNiceAgent": {
        "class": GWNiceAgent,
        "tags": ["AI-translated", "SHAOP", "SAOP"],
        "description": "Uses elicitation to learn preferences and mirroring strategy for offers",
    },
    "GWShineAgent": {
        "class": GWShineAgent,
        "tags": ["AI-translated", "SAOP"],
        "description": "Adaptive agent with dynamic strategy adjustment",
    },
}

__all__ = [
    # Raw agents
    "AgentKT",
    "AgentP1DAMO",
    "AgentXX",
    "AhBuNeAgent",
    "Anaconda",
    "Angel",
    "AzarAgent",
    "BlingBling",
    "DUOAgent",
    "ForArisa",
    "HammingAgent",
    "NiceAgent",
    "ShineAgent",
    # Wrapped agents
    "GWAgentKT",
    "GWAgentP1DAMO",
    "GWAgentXX",
    "GWAhBuNeAgent",
    "GWAnaconda",
    "GWAngel",
    "GWAzarAgent",
    "GWBlingBling",
    "GWDUOAgent",
    "GWForArisa",
    "GWHammingAgent",
    "GWNiceAgent",
    "GWShineAgent",
    # Dictionaries
    "AGENTS",
    "WRAPPED_AGENTS",
    # Metadata
    "AGENT_METADATA",
    "WRAPPED_AGENT_METADATA",
]
