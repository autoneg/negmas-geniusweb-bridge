"""
ANL 2022 Agents - Python Native.

Agents from the Automated Negotiation League 2022 competition.
These agents were originally written in Python by their authors.

Note: Some agents have known issues and are marked accordingly.
"""

from typing import Any

from ..wrapper import make_geniusweb_negotiator

# Import raw agents - all agents that can be imported
from .agent007.agent007 import Agent007
from .agent4410.agent_4410 import Agent4410
from .agentfish.agentfish import AgentFish
from .AgentFO2.AgentFO2 import AgentFO2
from .BIU_agent.BIU_agent import BIU_agent
from .charging_boul.charging_boul import ChargingBoul
from .compromising_agent.compromising_agent import CompromisingAgent
from .dreamteam109_agent.dreamteam109_agent import DreamTeam109Agent
from .gea_agent.gea_agent import GEAAgent
from .learning_agent.learning_agent import LearningAgent
from .LuckyAgent2022.LuckyAgent2022 import LuckyAgent2022
from .micro_agent.micro_agent.micro_agent import MiCROAgent
from .procrastin_agent.procrastin_agent import ProcrastinAgent
from .rg_agent.rg_agent import RGAgent
from .smart_agent.smart_agent import SmartAgent
from .super_agent.super_agent import SuperAgent
from .thirdagent.third_agent import ThirdAgent
from .tjaronchery10_agent.tjaronchery10_agent import Tjaronchery10Agent

# Pinar_Agent requires lightgbm - make it optional
try:
    from .Pinar_Agent.Pinar_Agent import Pinar_Agent

    PINAR_AGENT_AVAILABLE = True
except ImportError:
    Pinar_Agent = None  # type: ignore[misc, assignment]
    PINAR_AGENT_AVAILABLE = False

# Dictionary of raw GeniusWeb party classes
# All agents are included, with notes about known issues
AGENTS: dict[str, Any] = {
    "Agent007": Agent007,
    "Agent4410": Agent4410,
    "AgentFish": AgentFish,
    "AgentFO2": AgentFO2,
    "BIU_agent": BIU_agent,  # NOTE: may timeout >60 secs on some domains
    "ChargingBoul": ChargingBoul,
    "CompromisingAgent": CompromisingAgent,  # NOTE: may cause Action cannot be None errors
    "DreamTeam109Agent": DreamTeam109Agent,
    "GEAAgent": GEAAgent,  # NOTE: slow, a turn takes ~1.5sec
    "LearningAgent": LearningAgent,  # NOTE: may cause Action cannot be None errors
    "LuckyAgent2022": LuckyAgent2022,
    "MiCROAgent": MiCROAgent,
    "ProcrastinAgent": ProcrastinAgent,  # NOTE: may have issues with first offer accepted
    "RGAgent": RGAgent,
    "SmartAgent": SmartAgent,
    "SuperAgent": SuperAgent,
    "ThirdAgent": ThirdAgent,
    "Tjaronchery10Agent": Tjaronchery10Agent,
}

# Add Pinar_Agent if available
if PINAR_AGENT_AVAILABLE:
    AGENTS["Pinar_Agent"] = Pinar_Agent

# Agent metadata with notes about known issues
AGENT_NOTES: dict[str, str] = {
    "BIU_agent": "May timeout >60 secs on some domains",
    "CompromisingAgent": "May cause 'Action cannot be None' errors",
    "GEAAgent": "Slow execution, ~1.5sec per turn",
    "LearningAgent": "May cause 'Action cannot be None' errors",
    "ProcrastinAgent": "May have issues handling first offer accepted",
    "Pinar_Agent": "Requires lightgbm package",
}

# Create GW-prefixed wrapped negotiator classes
GWAgent007 = make_geniusweb_negotiator(Agent007)
GWAgent4410 = make_geniusweb_negotiator(Agent4410)
GWAgentFish = make_geniusweb_negotiator(AgentFish)
GWAgentFO2 = make_geniusweb_negotiator(AgentFO2)
GWBIU_agent = make_geniusweb_negotiator(BIU_agent)
GWChargingBoul = make_geniusweb_negotiator(ChargingBoul)
GWCompromisingAgent = make_geniusweb_negotiator(CompromisingAgent)
GWDreamTeam109Agent = make_geniusweb_negotiator(DreamTeam109Agent)
GWGEAAgent = make_geniusweb_negotiator(GEAAgent)
GWLearningAgent = make_geniusweb_negotiator(LearningAgent)
GWLuckyAgent2022 = make_geniusweb_negotiator(LuckyAgent2022)
GWMiCROAgent = make_geniusweb_negotiator(MiCROAgent)
GWProcrastinAgent = make_geniusweb_negotiator(ProcrastinAgent)
GWRGAgent = make_geniusweb_negotiator(RGAgent)
GWSmartAgent = make_geniusweb_negotiator(SmartAgent)
GWSuperAgent = make_geniusweb_negotiator(SuperAgent)
GWThirdAgent = make_geniusweb_negotiator(ThirdAgent)
GWTjaronchery10Agent = make_geniusweb_negotiator(Tjaronchery10Agent)

# Dictionary of wrapped negotiator classes
WRAPPED_AGENTS: dict[str, Any] = {
    "GWAgent007": GWAgent007,
    "GWAgent4410": GWAgent4410,
    "GWAgentFish": GWAgentFish,
    "GWAgentFO2": GWAgentFO2,
    "GWBIU_agent": GWBIU_agent,
    "GWChargingBoul": GWChargingBoul,
    "GWCompromisingAgent": GWCompromisingAgent,
    "GWDreamTeam109Agent": GWDreamTeam109Agent,
    "GWGEAAgent": GWGEAAgent,
    "GWLearningAgent": GWLearningAgent,
    "GWLuckyAgent2022": GWLuckyAgent2022,
    "GWMiCROAgent": GWMiCROAgent,
    "GWProcrastinAgent": GWProcrastinAgent,
    "GWRGAgent": GWRGAgent,
    "GWSmartAgent": GWSmartAgent,
    "GWSuperAgent": GWSuperAgent,
    "GWThirdAgent": GWThirdAgent,
    "GWTjaronchery10Agent": GWTjaronchery10Agent,
}

# Add GWPinar_Agent if available
if PINAR_AGENT_AVAILABLE:
    GWPinar_Agent = make_geniusweb_negotiator(Pinar_Agent)
    WRAPPED_AGENTS["GWPinar_Agent"] = GWPinar_Agent
else:
    GWPinar_Agent = None  # type: ignore[misc, assignment]

__all__ = [
    # Availability flags
    "PINAR_AGENT_AVAILABLE",
    # Raw agents
    "Agent007",
    "Agent4410",
    "AgentFish",
    "AgentFO2",
    "BIU_agent",
    "ChargingBoul",
    "CompromisingAgent",
    "DreamTeam109Agent",
    "GEAAgent",
    "LearningAgent",
    "LuckyAgent2022",
    "MiCROAgent",
    "Pinar_Agent",
    "ProcrastinAgent",
    "RGAgent",
    "SmartAgent",
    "SuperAgent",
    "ThirdAgent",
    "Tjaronchery10Agent",
    # Wrapped agents
    "GWAgent007",
    "GWAgent4410",
    "GWAgentFish",
    "GWAgentFO2",
    "GWBIU_agent",
    "GWChargingBoul",
    "GWCompromisingAgent",
    "GWDreamTeam109Agent",
    "GWGEAAgent",
    "GWLearningAgent",
    "GWLuckyAgent2022",
    "GWMiCROAgent",
    "GWPinar_Agent",
    "GWProcrastinAgent",
    "GWRGAgent",
    "GWSmartAgent",
    "GWSuperAgent",
    "GWThirdAgent",
    "GWTjaronchery10Agent",
    # Dictionaries
    "AGENTS",
    "WRAPPED_AGENTS",
    "AGENT_NOTES",
]
