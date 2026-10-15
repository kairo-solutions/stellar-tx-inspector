# Python API reference

## `inspect_transaction`

```python
from stellar_tx_inspector import inspect_transaction

report = inspect_transaction(
    xdr,
    network="testnet",
    custom_passphrase=None,
)
```

`xdr` is a base64 transaction envelope string. `network` must be `public`,
`testnet`, or `custom`. For a custom network, supply its passphrase as
`custom_passphrase`.

The function returns a dictionary with:

| Field | Description |
| --- | --- |
| `network` | Selected network label |
| `transaction_hash` | Envelope hash computed for the selected network |
| `source_account` | Transaction source account |
| `sequence` | Transaction sequence number |
| `fee_stroops` | Transaction fee in stroops |
| `signature_count` | Number of signatures in the envelope |
| `operation_count` | Number of operations |
| `operations` | Ordered operation type, index, and optional source |

Soroban `InvokeHostFunction` operations also include
`soroban_auth_entry_count`.

## Errors and limitations

Invalid network selections, empty XDR, over-limit input, and malformed
envelopes raise `ValueError`. The input is limited to 1 MB.

The SDK parses XDR; the report is descriptive only. It does not verify
signatures, simulate operations, or submit transactions.
