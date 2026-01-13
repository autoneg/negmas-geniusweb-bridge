# Wrapper Classes

This module provides wrapper classes that allow GeniusWeb agents to work seamlessly within NegMAS mechanisms.

## GeniusWebNegotiator

The main wrapper class that adapts GeniusWeb `DefaultParty` agents to work as NegMAS `SAONegotiator` instances.

::: negmas_geniusweb_bridge.wrapper.GeniusWebNegotiator
    options:
      show_source: true
      members:
        - __init__
        - propose
        - respond
        - on_partner_proposal
        - on_partner_response

## Helper Functions

### ufun_to_geniusweb

Convert a NegMAS utility function to a GeniusWeb `LinearAdditive` utility space.

::: negmas_geniusweb_bridge.wrapper.ufun_to_geniusweb

### outcome_to_bid

Convert a NegMAS outcome to a GeniusWeb `Bid`.

::: negmas_geniusweb_bridge.wrapper.outcome_to_bid

### bid_to_outcome

Convert a GeniusWeb `Bid` to a NegMAS outcome.

::: negmas_geniusweb_bridge.wrapper.bid_to_outcome

## Usage Example

```python
from negmas import SAOMechanism
from negmas.preferences import LinearAdditiveUtilityFunction
from negmas_geniusweb_bridge import GeniusWebNegotiator
from negmas_geniusweb_bridge.basic.random_agent import RandomAgent

# Create a mechanism
mechanism = SAOMechanism(
    issues=issues,
    n_steps=100
)

# Create a GeniusWeb agent wrapped for NegMAS
negotiator = GeniusWebNegotiator(
    geniusweb_agent_class=RandomAgent,
    name="random_agent"
)

# Add to mechanism with utility function
mechanism.add(negotiator, ufun=my_ufun)

# Run the negotiation
mechanism.run()
```
