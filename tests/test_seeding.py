"""Tests that a run is reproducible when the global generators are seeded.

Several wrapped agents build their own :class:`random.Random`. Seeding it from
the global :mod:`random` stream is what makes them follow the seed of the run,
whether that seed is set by hand or by negmas through ``NEGMAS_RAND_SEED``.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

import pytest

# Agents that build their own random.Random and whose offers depend on it
SEED_SENSITIVE_AGENTS = ["AhBuNeAgent", "MatrixAlienAgent"]

_SCRIPT = """
import warnings

warnings.filterwarnings("ignore")
import random
import sys

from negmas import SAOMechanism, make_issue
from negmas.preferences import LinearAdditiveUtilityFunction
from negmas.sao import AspirationNegotiator

import negmas_geniusweb_bridge as bridge

if sys.argv[2] != "none":
    random.seed(int(sys.argv[2]))
issues = [make_issue(7, "price"), make_issue(5, "quality"), make_issue(4, "delivery")]
ufun_a = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)
ufun_b = LinearAdditiveUtilityFunction.random(issues=issues, normalized=True)
mechanism = SAOMechanism(issues=issues, n_steps=20)
mechanism.add(bridge.ALL_AGENTS[sys.argv[1]](name="gw", ufun=ufun_a))
mechanism.add(AspirationNegotiator(name="asp", ufun=ufun_b))
mechanism.run()
for step in mechanism.trace:
    print(step)
print("agreement", mechanism.agreement)
"""

_UUID = re.compile(r"-[0-9a-f-]{36}")


def _run(agent: str, seed: int | None, env_seed: str | None = None) -> str:
    """Run one negotiation in a fresh interpreter and return its trace.

    Args:
        agent: name of the wrapped agent to run against `AspirationNegotiator`.
        seed: passed to `random.seed` inside the subprocess (`None` seeds nothing).
        env_seed: value of ``NEGMAS_RAND_SEED`` (`None` removes it).
    """
    env = dict(os.environ)
    # negotiator ids are uuid4 based and hash randomization reorders bid sets;
    # neither is part of what seeding the random generators covers.
    env["PYTHONHASHSEED"] = "0"
    if env_seed is None:
        env.pop("NEGMAS_RAND_SEED", None)
    else:
        env["NEGMAS_RAND_SEED"] = env_seed
    result = subprocess.run(
        [sys.executable, "-c", _SCRIPT, agent, "none" if seed is None else str(seed)],
        capture_output=True,
        text=True,
        env=env,
        timeout=300,
    )
    assert result.returncode == 0, result.stderr
    return _UUID.sub("", result.stdout)


@pytest.mark.parametrize("agent", SEED_SENSITIVE_AGENTS)
def test_seeded_runs_are_reproducible(agent):
    """The same seed gives the same negotiation in two separate processes."""
    assert _run(agent, 42) == _run(agent, 42)


@pytest.mark.parametrize("agent", SEED_SENSITIVE_AGENTS)
def test_different_seeds_give_different_runs(agent):
    """The seed really reaches the agents' own generators."""
    assert _run(agent, 42) != _run(agent, 1234)


@pytest.mark.parametrize("agent", SEED_SENSITIVE_AGENTS)
def test_negmas_rand_seed_is_enough(agent):
    """negmas' own global seed reproduces the run without any explicit seeding."""
    pytest.importorskip(
        "negmas.helpers.rand", reason="installed negmas has no global seeding"
    )
    assert _run(agent, None, env_seed="42") == _run(agent, None, env_seed="42")


def test_import_without_a_seed():
    """Importing the package with no seed set must keep working."""
    env = dict(os.environ)
    env.pop("NEGMAS_RAND_SEED", None)
    result = subprocess.run(
        [sys.executable, "-c", "import negmas_geniusweb_bridge"],
        capture_output=True,
        text=True,
        env=env,
        timeout=300,
    )
    assert result.returncode == 0, result.stderr
