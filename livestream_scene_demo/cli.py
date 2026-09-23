from __future__ import annotations

import argparse

from .io import read_windows, write_predictions
from .pipeline import ScenePipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="input JSONL windows")
    parser.add_argument("--output", required=True, help="output JSONL predictions")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    pipeline = ScenePipeline()
    predictions = [pipeline.process(window) for window in read_windows(args.input)]
    write_predictions(args.output, predictions)
    print(f"processed {len(predictions)} windows -> {args.output}")


if __name__ == "__main__":
    main()

