import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "stellar_tx_inspector.cli", "--help"],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Read-only inspection" in result.stdout
