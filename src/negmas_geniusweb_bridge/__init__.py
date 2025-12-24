from typing import Any
from .wrapper import make_geniusweb_negotiator as make_negotiator

from .ANL2022 import AGENTS as ANL2022_AGENTS
from .ANL2023 import AGENTS as ANL2023_AGENTS
from .basic import AGENTS as BASIC_AGENTS
from .CSE3210 import AGENTS as CSE3210_AGENTS

TRAINING_AGENTS: dict[str, Any] = {}
TESTING_AGENTS: dict[str, Any] = {}
ALL_AGENTS: dict[str, Any] = {}

ALL_AGENTS.update(
    {f"ANL2022_{k}": make_negotiator(v) for k, v in ANL2022_AGENTS.items()}
)
ALL_AGENTS.update(
    {f"ANL2023_{k}": make_negotiator(v) for k, v in ANL2023_AGENTS.items()}
)
ALL_AGENTS.update({f"BASIC_{k}": make_negotiator(v) for k, v in BASIC_AGENTS.items()})
ALL_AGENTS.update(
    {f"CSE3210_{k}": make_negotiator(v) for k, v in CSE3210_AGENTS.items()}
)
ALL_AGENTS.update(
    {f"ANL2022_{k}": make_negotiator(v) for k, v in ANL2022_AGENTS.items()}
)
ALL_AGENTS.update(
    {f"ANL2023_{k}": make_negotiator(v) for k, v in ANL2023_AGENTS.items()}
)
ALL_AGENTS.update(
    {f"CSE3210_{k}": make_negotiator(v) for k, v in CSE3210_AGENTS.items()}
)

TRAINING_AGENTS = ALL_AGENTS.copy()
TESTING_AGENTS = ALL_AGENTS.copy()
