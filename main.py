#!/usr/bin/env python3
"""meeting-email-01 — The Meeting That Should Have Been an Email.

Writes the one-line entry to /output/entry.txt.

The joke: a two-hour meeting held only to decide whether to send an
email — and the email, when it finally arrives, just quotes the meeting
back at everyone. Bureaucracy eating its own tail.
"""
import os

ENTRY = (
    'We held a two-hour meeting to decide whether to send an email. '
    'The email, when it finally arrived, said: "Per my last meeting."'
)

assert len(ENTRY) <= 200, "entry exceeds the 200-character cap"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
