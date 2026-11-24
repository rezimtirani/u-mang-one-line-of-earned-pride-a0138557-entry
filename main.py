#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes one line of quiet, earned pride to /output/entry.txt: a boy
who stutters reads a whole page aloud at assembly, and his little
sister is the first to clap.
"""

import os

LINE = "The boy who stuttered read the whole page aloud at assembly, and his little sister clapped first."


def gate_ok(text):
    """Check the competition gate: 1-240 characters, UTF-8, not only whitespace."""
    if not text or len(text) > 240:
        return False
    if not text.strip():
        return False
    text.encode("utf-8")
    return True


def verify_written(path, text):
    """Re-read the file and confirm it holds the entry byte for byte."""
    with open(path, "rb") as f:
        data = f.read()
    if data.decode("utf-8") != text:
        raise SystemExit("written file does not match the entry")
    if not gate_ok(data.decode("utf-8")):
        raise SystemExit("written file fails the gate")
    return len(data)


def main():
    if not gate_ok(LINE):
        raise SystemExit("entry fails the gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    verify_written(path, LINE)
    print("Wrote %s (%d characters)" % (path, len(LINE)))


if __name__ == "__main__":
    main()
