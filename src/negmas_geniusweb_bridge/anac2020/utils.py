"""
Common utilities for ANAC2020 agents.

This module provides shared functionality used by multiple agents,
including SimpleLinearOrdering which is used for bid ordering.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geniusweb.issuevalue.Bid import Bid
    from geniusweb.issuevalue.Domain import Domain


class SimpleLinearOrdering:
    """
    A simple list of bids, ordered from worst to best.

    This class maintains a linear ordering of bids where the first bid
    has utility 0 and the last bid has utility 1.
    """

    def __init__(self, domain: Domain, bids: list[Bid] | None = None):
        """
        Initialize the ordering.

        Args:
            domain: The negotiation domain.
            bids: A list of bids ordered from lowest to highest utility.
        """
        self._domain = domain
        self._bids: list[Bid] = list(bids) if bids else []

    @property
    def domain(self) -> Domain:
        """Get the domain."""
        return self._domain

    def get_domain(self) -> Domain:
        """Get the domain (Java-style method)."""
        return self._domain

    def getDomain(self) -> Domain:
        """Get the domain (GeniusWeb compatibility)."""
        return self._domain

    def get_bids(self) -> list[Bid]:
        """Get the list of bids."""
        return list(self._bids)

    def getBids(self) -> list[Bid]:
        """Get the list of bids (GeniusWeb compatibility)."""
        return self.get_bids()

    def size(self) -> int:
        """Get the number of bids."""
        return len(self._bids)

    def contains(self, bid: Bid) -> bool:
        """Check if a bid is in the ordering."""
        return bid in self._bids

    def get_utility(self, bid: Bid) -> Decimal:
        """
        Get the utility of a bid.

        Args:
            bid: The bid to evaluate.

        Returns:
            The utility as a Decimal between 0 and 1.
        """
        if len(self._bids) < 2 or bid not in self._bids:
            return Decimal(0)

        index = self._bids.index(bid)
        return Decimal(index) / Decimal(len(self._bids) - 1)

    def getUtility(self, bid: Bid) -> Decimal:
        """Get utility (GeniusWeb compatibility)."""
        return self.get_utility(bid)

    def with_bid(self, bid: Bid, worse_bids: list[Bid]) -> SimpleLinearOrdering:
        """
        Create a new ordering with an additional bid.

        Args:
            bid: The new bid to insert.
            worse_bids: All bids that are worse than this bid.

        Returns:
            A new SimpleLinearOrdering with the bid inserted.
        """
        n = 0
        while n < len(self._bids) and self._bids[n] in worse_bids:
            n += 1

        new_bids = list(self._bids)
        new_bids.insert(n, bid)
        return SimpleLinearOrdering(self._domain, new_bids)

    # Alias for Java-style method name
    def with_(self, bid: Bid, worse_bids: list[Bid]) -> SimpleLinearOrdering:
        """Alias for with_bid."""
        return self.with_bid(bid, worse_bids)


class OpponentModel:
    """
    A simple frequency-based opponent model.

    Tracks the frequency of issue-value selections by the opponent
    to estimate their preferences.
    """

    def __init__(self, domain: Domain):
        """
        Initialize the opponent model.

        Args:
            domain: The negotiation domain.
        """
        self._domain = domain
        self._issue_counts: dict[str, dict[str, int]] = {}
        self._total_bids = 0

        # Initialize counts for all issues and values
        for issue in domain.getIssues():
            self._issue_counts[issue] = {}
            value_set = domain.getValues(issue)
            for value in value_set:
                self._issue_counts[issue][str(value)] = 0

    def update(self, bid: Bid) -> None:
        """
        Update the model with a new opponent bid.

        Args:
            bid: The opponent's bid.
        """
        self._total_bids += 1
        for issue in bid.getIssues():
            value = bid.getValue(issue)
            if value is not None:
                value_str = str(value)
                if (
                    issue in self._issue_counts
                    and value_str in self._issue_counts[issue]
                ):
                    self._issue_counts[issue][value_str] += 1

    def get_predicted_utility(self, bid: Bid) -> float:
        """
        Get the predicted utility of a bid for the opponent.

        Args:
            bid: The bid to evaluate.

        Returns:
            A value between 0 and 1 representing predicted opponent utility.
        """
        if self._total_bids == 0:
            return 0.5

        total_score = 0.0
        n_issues = len(bid.getIssues())

        for issue in bid.getIssues():
            value = bid.getValue(issue)
            if value is not None:
                value_str = str(value)
                if (
                    issue in self._issue_counts
                    and value_str in self._issue_counts[issue]
                ):
                    count = self._issue_counts[issue][value_str]
                    total_score += count / self._total_bids

        return total_score / n_issues if n_issues > 0 else 0.5
