"""Command-line interface for stellar-tx-inspector."""

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .inspector import inspect_transaction


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stellar-tx-inspect",
        description="Read-only inspection of a Stellar transaction envelope XDR.",
    )
    parser.add_argument(
        "--input",
        default="-",
        help="XDR file to read, or - for standard input (default: -)",
    )
    parser.add_argument(
        "--network",
        choices=("public", "testnet", "custom"),
        default="testnet",
        help="Network used when computing the transaction hash (default: testnet)",
    )
    parser.add_argument(
        "--network-passphrase",
        help="Passphrase required when --network=custom",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.input == "-":
            xdr = sys.stdin.read()
        else:
            xdr = Path(args.input).read_text(encoding="utf-8")
        report = inspect_transaction(xdr, args.network, args.network_passphrase)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
