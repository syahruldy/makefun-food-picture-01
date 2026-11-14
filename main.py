#!/usr/bin/env python3
"""food-picture-01 round 3: "Tonkotsu ramen, yolk mid-drip".

The top of the board is tonkotsu ramen with a tall noodle pull, so
this entry takes the whole winning frame and pushes its two most
dynamic details further: the pull is a full vertical column, and the
twin jammy eggs are caught with the yolk falling in a long stream
onto the noodles. Charred chashu fan, chili-oil swirl, nori, steam,
warm bokeh behind a speckled bowl.

The program only carries the finished picture to the output folder.
"""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "art.jpg"  # 1024x1024 ramen


def main() -> None:
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    data = SOURCE.read_bytes()
    (output / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
