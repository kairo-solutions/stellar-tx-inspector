# Stellar Transaction Inspector

`stellar-tx-inspector` is a read-only Python CLI for decoding a Stellar
transaction envelope and summarizing its network-specific hash, source account,
sequence, fee, signatures, and operation types. It uses the official
`stellar-sdk` XDR parser; it does not submit transactions or need secret keys.

## Install and use

Requires Python 3.10 or newer.

```sh
python -m pip install .
stellar-tx-inspect --input transaction.xdr --network testnet
```

XDR can also be read from standard input, which avoids putting it directly in
shell history:

```sh
cat transaction.xdr | stellar-tx-inspect --network public
```

For a private network, provide its passphrase:

```sh
stellar-tx-inspect --input transaction.xdr \
  --network custom \
  --network-passphrase "Private Stellar Network"
```

The output is JSON. The transaction hash depends on the selected network
passphrase. This tool decodes transaction structure and counts signatures; it
does not verify signature validity, simulate operations, or broadcast the
transaction.

## Development

```sh
uv sync --extra test
uv run pytest
```
