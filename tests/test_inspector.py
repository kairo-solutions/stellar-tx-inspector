import pytest
from stellar_sdk import Asset, Keypair, Payment, Transaction, TransactionEnvelope
from stellar_sdk.network import Network

from stellar_tx_inspector import inspect_transaction


def build_payment_xdr():
    source = Keypair.random()
    destination = Keypair.random()
    transaction = Transaction(
        source=source.public_key,
        sequence=42,
        fee=100,
        operations=[
            Payment(
                destination=destination.public_key,
                asset=Asset.native(),
                amount="1.25",
            )
        ],
    )
    envelope = TransactionEnvelope(
        transaction=transaction,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    )
    envelope.sign(source)
    return envelope.to_xdr(), envelope


def test_inspects_transaction_metadata_and_operations():
    xdr, envelope = build_payment_xdr()

    report = inspect_transaction(xdr, "testnet")

    assert report["network"] == "testnet"
    assert report["transaction_hash"] == envelope.hash_hex()
    assert report["source_account"] == envelope.transaction.source.account_id
    assert report["sequence"] == 42
    assert report["fee_stroops"] == 100
    assert report["signature_count"] == 1
    assert report["operation_count"] == 1
    assert report["operations"] == [{"index": 0, "type": "Payment"}]


def test_custom_network_requires_and_uses_passphrase():
    xdr, envelope = build_payment_xdr()
    passphrase = "Private Stellar Network"

    custom_envelope = TransactionEnvelope(
        transaction=envelope.transaction,
        network_passphrase=passphrase,
        signatures=envelope.signatures,
    )

    with pytest.raises(ValueError, match="custom network passphrase"):
        inspect_transaction(xdr, "custom")

    report = inspect_transaction(xdr, "custom", passphrase)
    assert report["transaction_hash"] == custom_envelope.hash_hex()


@pytest.mark.parametrize(
    ("xdr", "network", "message"),
    [
        ("", "testnet", "non-empty"),
        ("not-xdr", "testnet", "could not decode"),
        ("xdr", "unknown", "network must be"),
    ],
)
def test_rejects_invalid_input(xdr, network, message):
    with pytest.raises(ValueError, match=message):
        inspect_transaction(xdr, network)
