"""Notepad Encoding — Detect and convert a text file between UTF-8 and UTF-16 for Notepad."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='notepad_encoding',
        description='Detect and convert a text file between UTF-8 and UTF-16 for Notepad.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Notepad Encoding')
    print('The encoding Notepad actually saved.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
