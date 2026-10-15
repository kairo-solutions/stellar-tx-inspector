# Quick start

## Install

Requires Python 3.10 or newer:

```sh
python -m pip install stellar-tx-inspector
```

## Inspect from a file

```sh
stellar-tx-inspect --input transaction.xdr --network testnet
```

The command prints JSON containing the transaction hash, source, sequence, fee,
signature count, and operation types.

## Read from standard input

```sh
cat transaction.xdr | stellar-tx-inspect --network public
```

Standard input is the default, so XDR does not need to be passed as a command
argument or stored in shell history.

## Select a private network

```sh
stellar-tx-inspect \
  --input transaction.xdr \
  --network custom \
  --network-passphrase "Private Stellar Network"
```

A custom passphrase is necessary to compute the transaction hash for that
network. The output JSON does not include the passphrase.
