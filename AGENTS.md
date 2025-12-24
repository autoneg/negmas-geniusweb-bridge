# AGENTS.md

## Build/Test Commands
- Install: `uv sync`
- Run all tests: `uv run pytest`
- Run single test: `uv run pytest tests/test_negmas_wrapper.py::TestConversions::test_convert_ufun_to_geniusweb -v`
- Run test file: `uv run pytest tests/test_negmas_wrapper.py -v`

## Code Style
- **Python**: 3.13+, type hints required for function signatures
- **Imports**: Group as stdlib, third-party (geniusweb, negmas, numpy), local; use `from __future__ import annotations`
- **Formatting**: Double quotes for strings, 4-space indent
- **Types**: Use `TYPE_CHECKING` block for type-only imports; prefer `dict[str, Any]` over `Dict`
- **Naming**: snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- **Error handling**: Use `ValueError` with descriptive messages; check types explicitly before conversion
- **Optional imports**: Wrap in try/except with availability flag (e.g., `GENIUS_WEB_AVAILABLE`)
- **Docstrings**: Google-style with Args/Returns/Raises sections for public APIs
- **GeniusWeb agents**: Inherit from `DefaultParty`, implement `notifyChange()`, use `send_action()` or connection
- **Tests**: Use pytest fixtures, class-based test organization (`TestClassName`), descriptive method names
