"""
Quote data model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Quote:
    """One scraped quote row."""

    # Original top ten tag whose page contained the quote.
    tag: str

    # Quote author's displayed name.
    author: str

    # Quote text exactly as displayed on the page.
    quote: str
