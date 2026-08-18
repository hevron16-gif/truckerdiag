"""Audit knowledge base for collapsed / hidden codes."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "api"))
from knowledge import (  # noqa: E402
    EXTRA_KNOWLEDGE,
    KNOWLEDGE,
    _INDEX,
    _keep_alias,
    lookup,
    normalize_code,
)


def main() -> None:
    print("EXTRA", len(EXTRA_KNOWLEDGE), "KNOWLEDGE", len(KNOWLEDGE))
    print("index keys", len(_INDEX))
    print("multi keys", sum(1 for v in _INDEX.values() if len(v) > 1))

    leftover = []
    plus = 0
    for e in KNOWLEDGE:
        for a in e.get("aliases") or []:
            if "+" in str(a) or str(a).upper().startswith("DTC +"):
                plus += 1
            if not _keep_alias(str(a), str(e["code"])):
                leftover.append((e["code"], a))
    print("junk leftover after sanitize", len(leftover))
    print("aliases with +", plus)

    print("--- P001D family ---")
    for c in [
        "P001D",
        "P001A",
        "P001B",
        "P001C",
        "P001E",
        "P2609",
        "SPN 2898 FMI 17",
        "DTC P001D",
    ]:
        h = lookup(c)
        if h:
            print(c, "->", h["code"], "|", h["title"][:70])
        else:
            print(c, "-> MISSING")

    print("--- P0006 by engine ---")
    for eng, veh in [("WP12", "Shacman X3000"), ("MC11", "Howo T7H"), ("", "")]:
        h = lookup("P0006", engine=eng, brand=veh)
        src = h.get("source_system") if h else None
        print(eng or "-", veh or "-", "->", None if not h else f"{h['code']} [{src}] {h['title'][:55]}")

    for c in ("P0087", "U0100", "P1011"):
        h = lookup(c, engine="WP12", brand="Shacman X3000")
        print(c, "->", h["title"][:60] if h else "MISSING")

    hidden = 0
    wrong = 0
    for e in KNOWLEDGE:
        got = lookup(e["code"])
        if not got:
            hidden += 1
            if hidden <= 10:
                print("HIDDEN", e["code"], (e.get("title") or "")[:50], e.get("source_system"))
            continue
        if normalize_code(got["code"]) != normalize_code(e["code"]):
            wrong += 1
            if wrong <= 10:
                print(
                    "WRONG",
                    e["code"],
                    "got",
                    got["code"],
                    "|",
                    (e.get("title") or "")[:40],
                    "vs",
                    (got.get("title") or "")[:40],
                )
    print("primaries hidden", hidden, "primaries resolve to other card", wrong)

    ok = miss = 0
    tsv = Path(__file__).resolve().parent / "ramid.tsv"
    for line in tsv.read_text(encoding="utf-8").splitlines()[2:]:
        cols = line.split("\t")
        if len(cols) < 9:
            continue
        w = cols[7].strip().upper()
        if re.fullmatch(r"[PUC][0-9A-F]{4}", w):
            if lookup(w):
                ok += 1
            else:
                miss += 1
    print("weichai ok", ok, "miss", miss)


if __name__ == "__main__":
    main()
