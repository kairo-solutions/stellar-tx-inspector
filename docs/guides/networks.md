# Networks and transaction hashes

The XDR envelope contains transaction data, but the transaction hash is
computed from the envelope's signature base and a network ID. The same envelope
therefore has different hashes on different networks.

## Built-in networks

| `--network` | Passphrase |
| --- | --- |
| `public` | Stellar public network passphrase |
| `testnet` | Stellar test network passphrase (default) |

For any other network, choose `custom` and provide
`--network-passphrase`. A missing custom passphrase is an input error; the tool
does not substitute a public-network default.

## Interpret the report

- `transaction_hash` is the hash for the selected network.
- `source_account`, `sequence`, and `fee_stroops` come from the decoded
  transaction.
- `signature_count` counts envelope signatures; it does not validate them.
- Each operation contains its index and SDK operation type. Operation-specific
  payloads are intentionally not decoded into a full simulation.

The inspector is a local parser. It neither checks whether a transaction is
valid at the current ledger nor submits it to Horizon or Soroban RPC.
