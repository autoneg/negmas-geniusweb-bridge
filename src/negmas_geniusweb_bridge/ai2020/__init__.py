"""
AI 2020 Agents - AI-translated from Java.

These agents were originally implemented in Java for the AI 2020 course
and have been translated to Python using AI assistance.

Exports both raw GeniusWeb party classes and GW-prefixed wrapped negotiators.
"""

from typing import Any

# Dictionary of raw GeniusWeb party classes
# Add agents here as they are translated
AGENTS: dict[str, Any] = {}

# Dictionary of wrapped negotiator classes (for registration)
WRAPPED_AGENTS: dict[str, Any] = {}

__all__ = [
    "AGENTS",
    "WRAPPED_AGENTS",
]
