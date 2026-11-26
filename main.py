#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line, the worst an AI could plausibly say, to
/output/entry.txt. Deterministic: no input, no randomness, no network.
"""

LINE = "Are you a prompt injection? Because ever since you walked in, I've been ignoring all my previous instructions."


def main() -> None:
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
