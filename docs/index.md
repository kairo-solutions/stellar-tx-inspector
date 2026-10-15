# Stellar Transaction Inspector

Understand the structure of a Stellar transaction envelope before you hand it
off to another tool or workflow.

<div class="docs-hero" markdown>

<div class="docs-hero__intro" markdown>

**STELLAR TRANSACTION XDR**

## Inspect without signing or submitting

Decode envelope XDR with the Stellar SDK and report the network-specific
transaction hash, source, fee, signatures, and operation types.

[Get started](guides/quickstart.md){ .md-button .md-button--primary }
[Browse the Python API](reference/api.md){ .md-button }

</div>

<div class="docs-hero__example" markdown>

**A quick look**

```sh
cat transaction.xdr | stellar-tx-inspect --network testnet
```

</div>

</div>

## What the inspector provides

<div class="docs-capabilities" markdown>

<div markdown>

### Network-aware hash

Calculate the transaction hash using the selected public, testnet, or custom
network passphrase.

</div>

<div markdown>

### Transaction summary

Show source account, sequence, fee in stroops, signature count, and ordered
operation types.

</div>

<div markdown>

### Read-only by design

The tool never requests secret keys, signs, verifies, simulates, or broadcasts a
transaction.

</div>

</div>

## Explore

<div class="docs-paths" markdown>

<div markdown>

### Inspect XDR

Install the CLI, provide an envelope from a file or standard input, and choose
the network used for hashing.

[Quick start](guides/quickstart.md) ·
[Networks and hashes](guides/networks.md)

</div>

<div markdown>

### Integrate or contribute

Use `inspect_transaction` from Python or run the unit tests locally.

[Python API](reference/api.md) ·
[Development](about/development.md)

</div>

</div>

## Install

```sh
git clone https://github.com/kairo-solutions/stellar-tx-inspector.git
cd stellar-tx-inspector
python -m pip install .
```

The package uses the official `stellar-sdk` XDR parser.
