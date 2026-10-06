#!/usr/bin/env python3
"""Verify that quotes in a JSON result are exact substrings of a transcript."""

import argparse
import json
from pathlib import Path


def collect_quotes(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"quote", "text"} and isinstance(item, str) and item.strip():
                yield item
            else:
                yield from collect_quotes(item)
    elif isinstance(value, list):
        for item in value:
            yield from collect_quotes(item)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()

    transcript = args.transcript.read_text(encoding="utf-8")
    result = json.loads(args.result.read_text(encoding="utf-8"))
    quotes = list(dict.fromkeys(collect_quotes(result)))
    failures = []
    for quote in quotes:
        offset = transcript.find(quote)
        if offset < 0:
            failures.append(quote)
        else:
            print(json.dumps({"quote": quote, "start": offset, "end": offset + len(quote)}))

    print(json.dumps({"checked": len(quotes), "valid": len(quotes) - len(failures), "invalid": len(failures)}))
    if failures:
        for quote in failures:
            print(json.dumps({"invalid_quote": quote}))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
