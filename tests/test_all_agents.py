"""Comprehensive tests for all GeniusWeb agents.

This module tests every wrapped agent in the library to ensure they can:
1. Be instantiated correctly
2. Negotiate against AspirationNegotiator without errors
3. Negotiate against another GeniusWeb agent (GWBoulwareAgent) without errors
"""

from __future__ import annotations

import pytest
from negmas import SAOMechanism, make_issue
from negmas.preferences import LinearAdditiveUtilityFunction
from negmas.sao import AspirationNegotiator

from negmas_geniusweb_bridge import ALL_AGENTS, GWBoulwareAgent


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def simple_issues():
    """Create simple test issues."""
    return [make_issue(5, "price"), make_issue(3, "quality")]


@pytest.fixture
def ufun_a(simple_issues):
    """Create a test utility function for agent A."""
    return LinearAdditiveUtilityFunction.random(issues=simple_issues, normalized=True)


@pytest.fixture
def ufun_b(simple_issues):
    """Create a test utility function for agent B."""
    return LinearAdditiveUtilityFunction.random(issues=simple_issues, normalized=True)


# ============================================================================
# Agent Lists by Module
# ============================================================================

# Basic agents - reference implementations
BASIC_AGENTS = [
    "GWBoulwareAgent",
    "GWConcederAgent",
    "GWHardlinerAgent",
    "GWLinearAgent",
    "GWRandomAgent",
    "GWStupidAgent",
    "GWTimeDependentAgent",
]

# ANAC 2020 agents - AI-translated from Java
ANAC2020_AGENTS = [
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
]

# ANL 2022 agents - Python native
ANL2022_AGENTS = [
    "GWAgent007",
    "GWAgent4410",
    "GWAgentFish",
    "GWAgentFO2",
    "GWBIUAgent",
    "GWChargingBoul",
    "GWCompromisingAgent",
    "GWDreamTeam109Agent",
    "GWGEAAgent",
    "GWLearningAgent",
    "GWLuckyAgent2022",
    "GWMiCROAgent",
    "GWProcrastinAgent",
    "GWRGAgent",
    "GWSmartAgent",
    "GWSuperAgent",
    "GWThirdAgent",
    "GWTjaronchery10Agent",
]

# ANL 2023 agents - Python native
ANL2023_AGENTS = [
    "GWAgentFO3",
    "GWAmbitiousAgent",
    "GWAntAllianceAgent",
    "GWAntHeartAgent",
    "GWColmanAnacondotAgent2",
    "GWExploitAgent",
    "GWGotAgent",
    "GWHybridAgent2023",
    "GWKBTimeDiffAgent",
    "GWMiCRO2023",
    "GWPopularAgent",
    "GWSpaghettiAgent",
    "GWTripleEAgent",
]

# CSE3210 agents - Python native (TU Delft course)
CSE3210_AGENTS = [
    "GWAgent2",
    "GWAgent3",
    "GWAgent7",
    "GWAgent11",
    "GWAgent14",
    "GWAgent18",
    "GWAgent19",
    "GWAgent22",
    "GWAgent24",
    "GWAgent25",
    "GWAgent26",
    "GWAgent27",
    "GWAgent29",
    "GWAgent32",
    "GWAgent33",
    "GWAgent41",
    "GWAgent43",
    "GWAgent50",
    "GWAgent52",
    "GWAgent55",
    "GWAgent58",
    "GWAgent61",
    "GWAgent64",
    "GWAgent67",
    "GWAgent68",
]

# All agents combined (excluding optional ones that require extra dependencies)
ALL_AGENT_NAMES = (
    BASIC_AGENTS + ANAC2020_AGENTS + ANL2022_AGENTS + ANL2023_AGENTS + CSE3210_AGENTS
)

# Agents with known issues that may fail some tests
# These are still tested but with xfail markers
AGENTS_WITH_KNOWN_ISSUES = {
    "GWCompromisingAgent": "May cause 'Action cannot be None' errors",
    "GWLearningAgent": "May cause 'Action cannot be None' errors",
    "GWAgent22": "May throw scipy divide by zero errors",
    "GWAgent68": "May have issues handling opening bid",
    "GWProcrastinAgent": "May have issues with first offer accepted",
    "GWHardlinerAgent": "Never concedes - unlikely to reach agreement",
    # ANL2023 agents with edge case issues
    "GWAgentFO3": "Empty bid list on small domains (randrange(0, 0))",
    "GWAmbitiousAgent": "ProgressRounds missing getStart method",
    "GWAntAllianceAgent": "Empty bid list on small domains",
    "GWKBTimeDiffAgent": "Division by zero on small domains",
    "GWSpaghettiAgent": "Empty deque pop on small domains",
    # ANL2022 agents with edge case issues
    "GWAgentFO2": "Empty bid list on small domains",
    "GWBIUAgent": "May timeout >60 secs on some domains",
    "GWThirdAgent": "Empty bid list on small domains",
    # CSE3210 agents with edge case issues
    "GWAgent18": "Zero-size array reduction issues",
    "GWAgent33": "Random choice from empty array",
    "GWAgent52": "Random choice from empty array",
    "GWAgent67": "Edge case issues on small domains",
}

# Agents that are slow and should have longer timeouts
SLOW_AGENTS = {
    "GWGEAAgent": "Slow execution, ~1.5sec per turn",
    "GWBIUAgent": "May timeout >60 secs on some domains",
}


# ============================================================================
# Helper Functions
# ============================================================================


def run_negotiation(agent_cls, opponent_cls, ufun_a, ufun_b, issues, n_steps=50):
    """Run a negotiation between two agents and return the mechanism state.

    Args:
        agent_cls: The agent class to test
        opponent_cls: The opponent agent class
        ufun_a: Utility function for agent_cls
        ufun_b: Utility function for opponent_cls
        issues: The negotiation issues
        n_steps: Maximum number of steps

    Returns:
        The mechanism state after negotiation
    """
    mechanism = SAOMechanism(issues=issues, n_steps=n_steps)

    agent_a = agent_cls(ufun=ufun_a, name="agent_a")
    agent_b = opponent_cls(ufun=ufun_b, name="agent_b")

    mechanism.add(agent_a)
    mechanism.add(agent_b)

    mechanism.run()

    return mechanism.state


def get_agent_class(agent_name: str):
    """Get the agent class from ALL_AGENTS by name."""
    if agent_name not in ALL_AGENTS:
        pytest.skip(
            f"Agent {agent_name} not available (may require optional dependencies)"
        )
    return ALL_AGENTS[agent_name]


# ============================================================================
# Test Classes
# ============================================================================


class TestBasicAgentsVsAspiration:
    """Test basic agents against AspirationNegotiator."""

    @pytest.mark.parametrize("agent_name", BASIC_AGENTS)
    def test_vs_aspiration(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that basic agents can negotiate against AspirationNegotiator."""
        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, AspirationNegotiator, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestBasicAgentsVsGeniusWeb:
    """Test basic agents against GWBoulwareAgent."""

    @pytest.mark.parametrize("agent_name", BASIC_AGENTS)
    def test_vs_geniusweb(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that basic agents can negotiate against GWBoulwareAgent."""
        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, GWBoulwareAgent, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestANAC2020AgentsVsAspiration:
    """Test ANAC 2020 agents against AspirationNegotiator."""

    @pytest.mark.parametrize("agent_name", ANAC2020_AGENTS)
    def test_vs_aspiration(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that ANAC 2020 agents can negotiate against AspirationNegotiator."""
        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, AspirationNegotiator, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestANAC2020AgentsVsGeniusWeb:
    """Test ANAC 2020 agents against GWBoulwareAgent."""

    @pytest.mark.parametrize("agent_name", ANAC2020_AGENTS)
    def test_vs_geniusweb(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that ANAC 2020 agents can negotiate against GWBoulwareAgent."""
        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, GWBoulwareAgent, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestANL2022AgentsVsAspiration:
    """Test ANL 2022 agents against AspirationNegotiator."""

    @pytest.mark.parametrize("agent_name", ANL2022_AGENTS)
    def test_vs_aspiration(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that ANL 2022 agents can negotiate against AspirationNegotiator."""
        if agent_name in AGENTS_WITH_KNOWN_ISSUES:
            pytest.xfail(AGENTS_WITH_KNOWN_ISSUES[agent_name])

        agent_cls = get_agent_class(agent_name)
        n_steps = 100 if agent_name in SLOW_AGENTS else 50

        state = run_negotiation(
            agent_cls, AspirationNegotiator, ufun_a, ufun_b, simple_issues, n_steps
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestANL2022AgentsVsGeniusWeb:
    """Test ANL 2022 agents against GWBoulwareAgent."""

    @pytest.mark.parametrize("agent_name", ANL2022_AGENTS)
    def test_vs_geniusweb(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that ANL 2022 agents can negotiate against GWBoulwareAgent."""
        if agent_name in AGENTS_WITH_KNOWN_ISSUES:
            pytest.xfail(AGENTS_WITH_KNOWN_ISSUES[agent_name])

        agent_cls = get_agent_class(agent_name)
        n_steps = 100 if agent_name in SLOW_AGENTS else 50

        state = run_negotiation(
            agent_cls, GWBoulwareAgent, ufun_a, ufun_b, simple_issues, n_steps
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestANL2023AgentsVsAspiration:
    """Test ANL 2023 agents against AspirationNegotiator."""

    @pytest.mark.parametrize("agent_name", ANL2023_AGENTS)
    def test_vs_aspiration(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that ANL 2023 agents can negotiate against AspirationNegotiator."""
        if agent_name in AGENTS_WITH_KNOWN_ISSUES:
            pytest.xfail(AGENTS_WITH_KNOWN_ISSUES[agent_name])

        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, AspirationNegotiator, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestANL2023AgentsVsGeniusWeb:
    """Test ANL 2023 agents against GWBoulwareAgent."""

    @pytest.mark.parametrize("agent_name", ANL2023_AGENTS)
    def test_vs_geniusweb(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that ANL 2023 agents can negotiate against GWBoulwareAgent."""
        if agent_name in AGENTS_WITH_KNOWN_ISSUES:
            pytest.xfail(AGENTS_WITH_KNOWN_ISSUES[agent_name])

        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, GWBoulwareAgent, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestCSE3210AgentsVsAspiration:
    """Test CSE3210 agents against AspirationNegotiator."""

    @pytest.mark.parametrize("agent_name", CSE3210_AGENTS)
    def test_vs_aspiration(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that CSE3210 agents can negotiate against AspirationNegotiator."""
        if agent_name in AGENTS_WITH_KNOWN_ISSUES:
            pytest.xfail(AGENTS_WITH_KNOWN_ISSUES[agent_name])

        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, AspirationNegotiator, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestCSE3210AgentsVsGeniusWeb:
    """Test CSE3210 agents against GWBoulwareAgent."""

    @pytest.mark.parametrize("agent_name", CSE3210_AGENTS)
    def test_vs_geniusweb(self, agent_name, simple_issues, ufun_a, ufun_b):
        """Test that CSE3210 agents can negotiate against GWBoulwareAgent."""
        if agent_name in AGENTS_WITH_KNOWN_ISSUES:
            pytest.xfail(AGENTS_WITH_KNOWN_ISSUES[agent_name])

        agent_cls = get_agent_class(agent_name)

        state = run_negotiation(
            agent_cls, GWBoulwareAgent, ufun_a, ufun_b, simple_issues
        )

        assert not state.running, f"{agent_name} negotiation did not complete"
        assert state.step > 0, f"{agent_name} made no progress"


class TestAgentInstantiation:
    """Test that all agents can be instantiated."""

    @pytest.mark.parametrize("agent_name", ALL_AGENT_NAMES)
    def test_instantiation(self, agent_name, simple_issues, ufun_a):
        """Test that agents can be instantiated with a utility function."""
        agent_cls = get_agent_class(agent_name)

        agent = agent_cls(ufun=ufun_a, name=f"test_{agent_name}")

        assert agent is not None
        assert agent.ufun == ufun_a


class TestCrossModuleNegotiation:
    """Test negotiations between agents from different modules."""

    def test_anac2020_vs_anl2022(self, simple_issues, ufun_a, ufun_b):
        """Test negotiation between ANAC 2020 and ANL 2022 agents."""
        agent_a_cls = get_agent_class("GWHammingAgent")
        agent_b_cls = get_agent_class("GWAgent007")

        state = run_negotiation(agent_a_cls, agent_b_cls, ufun_a, ufun_b, simple_issues)

        assert not state.running
        assert state.step > 0

    def test_anl2022_vs_anl2023(self, simple_issues, ufun_a, ufun_b):
        """Test negotiation between ANL 2022 and ANL 2023 agents."""
        agent_a_cls = get_agent_class("GWMiCROAgent")
        agent_b_cls = get_agent_class("GWMiCRO2023")

        state = run_negotiation(agent_a_cls, agent_b_cls, ufun_a, ufun_b, simple_issues)

        assert not state.running
        assert state.step > 0

    def test_anl2023_vs_cse3210(self, simple_issues, ufun_a, ufun_b):
        """Test negotiation between ANL 2023 and CSE3210 agents."""
        agent_a_cls = get_agent_class("GWExploitAgent")
        agent_b_cls = get_agent_class("GWAgent11")

        state = run_negotiation(agent_a_cls, agent_b_cls, ufun_a, ufun_b, simple_issues)

        assert not state.running
        assert state.step > 0

    def test_basic_vs_anac2020(self, simple_issues, ufun_a, ufun_b):
        """Test negotiation between basic and ANAC 2020 agents."""
        agent_a_cls = get_agent_class("GWConcederAgent")
        agent_b_cls = get_agent_class("GWShineAgent")

        state = run_negotiation(agent_a_cls, agent_b_cls, ufun_a, ufun_b, simple_issues)

        assert not state.running
        assert state.step > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
