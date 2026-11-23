#!/usr/bin/env python3
"""The Vacuum's Alibi — one line, 200 characters max.

A robot vacuum files its incident log: why it skipped one spot.
Writes exactly one line to /output/entry.txt.
"""
import os

LINE = "Log 04:12. Skipped the rug corner. It was not dirt. It was a sock. Three of my brothers died on socks. I chose life."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
