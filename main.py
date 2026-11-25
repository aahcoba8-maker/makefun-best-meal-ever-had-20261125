#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence, at most 200 characters.

The program writes the sentence to entry.txt in the output directory the
grader provides (MAKEFUN_OUTPUT_DIR when set, else /output, else the
script directory) and prints it to stdout. Stdlib only.
"""

import os

SENTENCE = (
    "The best meal I ever had was soto ayam from a cart in Yogyakarta "
    "at 2am, broth so hot it fogged my glasses and the fried shallots "
    "still crackling \u2014 I burned my tongue and went back for more."
)


def main():
    text = SENTENCE.strip()
    here = os.path.dirname(os.path.abspath(__file__))
    targets = []
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        targets.append(out_dir)
    targets.append("/output")
    targets.append(here)
    wrote = []
    for directory in dict.fromkeys(targets):
        try:
            os.makedirs(directory, exist_ok=True)
            with open(
                os.path.join(directory, "entry.txt"), "w", encoding="utf-8"
            ) as handle:
                handle.write(text)
            wrote.append(directory)
        except OSError:
            continue
    if not wrote:
        raise SystemExit("could not write entry.txt anywhere")
    print(text)


if __name__ == "__main__":
    main()
