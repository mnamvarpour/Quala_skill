#!/usr/bin/env python3
"""Return true when a non-empty quote is an exact substring of a source."""

import argparse


def quote_is_in_source(source: str, quote: str) -> bool:
    """Return whether quote occurs exactly and contiguously in source."""
    return bool(quote) and quote in source


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Source text")
    parser.add_argument("quote", help="Candidate quote")
    args = parser.parse_args()
    print(str(quote_is_in_source(args.source, args.quote)).lower())


if __name__ == "__main__":
    main()
