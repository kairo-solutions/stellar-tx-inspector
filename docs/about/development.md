# Development

## Requirements

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/) for reproducible development dependencies

## Run tests and the CLI

```sh
uv sync --extra test
uv run pytest
uv run stellar-tx-inspect --help
```

Tests construct envelopes locally and do not connect to Stellar services.

## Contribution scope

Keep the inspector read-only. Changes to parsed fields should include test
envelopes and document any limits or behavior not guaranteed by the SDK.
