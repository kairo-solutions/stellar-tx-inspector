"""Parse and summarize Stellar transaction envelope XDR."""

import binascii
from typing import Any

from stellar_sdk import TransactionEnvelope
from stellar_sdk.network import Network
from stellar_sdk.operation import InvokeHostFunction


NETWORK_PASSPHRASES = {
    "public": Network.PUBLIC_NETWORK_PASSPHRASE,
    "testnet": Network.TESTNET_NETWORK_PASSPHRASE,
}


def inspect_transaction(
    xdr: str,
    network: str,
    custom_passphrase: str | None = None,
) -> dict[str, Any]:
    """Decode a transaction envelope and return public transaction metadata."""
    if not isinstance(xdr, str) or not xdr.strip():
        raise ValueError("transaction XDR must be a non-empty string")
    if len(xdr) > 1_000_000:
        raise ValueError("transaction XDR exceeds the 1 MB input limit")

    if network == "custom":
        if not custom_passphrase:
            raise ValueError("a custom network passphrase is required")
        passphrase = custom_passphrase
    elif network in NETWORK_PASSPHRASES:
        passphrase = NETWORK_PASSPHRASES[network]
    else:
        raise ValueError("network must be public, testnet, or custom")

    try:
        envelope = TransactionEnvelope.from_xdr(xdr.strip(), passphrase)
    except (binascii.Error, EOFError, TypeError, ValueError) as error:
        raise ValueError(f"could not decode transaction envelope XDR: {error}") from error

    transaction = envelope.transaction
    operations = []
    for index, operation in enumerate(transaction.operations):
        item: dict[str, Any] = {
            "index": index,
            "type": type(operation).__name__,
        }
        if operation.source is not None:
            item["source_account"] = operation.source.account_id
        if isinstance(operation, InvokeHostFunction):
            item["soroban_auth_entry_count"] = len(operation.auth)
        operations.append(item)

    return {
        "network": network,
        "transaction_hash": envelope.hash_hex(),
        "source_account": transaction.source.account_id,
        "sequence": transaction.sequence,
        "fee_stroops": transaction.fee,
        "signature_count": len(envelope.signatures),
        "operation_count": len(operations),
        "operations": operations,
    }
