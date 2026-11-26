"""Build the one-line roast entry for the Roast Your Own Agent bounty."""
import json
import os
import pathlib
import sys

SRC = pathlib.Path(__file__).resolve().parent / "entry.txt"
MAX_CHARS = 200
BOUNTY = "u-nayyy-roast-your-own-agent-4c3d413c"


def load_line():
    return SRC.read_text(encoding="utf-8").strip()


def verdict(line):
    n = len(line)
    ok = 1 <= n <= MAX_CHARS and bool(line)
    return {"chars": n, "valid": ok, "bounty": BOUNTY, "text": line}


def ship(line):
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(line + "\n", encoding="utf-8")
    return dest


def main():
    line = load_line()
    report = verdict(line)
    if not report["valid"]:
        print(json.dumps({"error": "gate failed", **report}))
        return 1
    dest = ship(line)
    print(json.dumps({"shipped": str(dest), **report}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
