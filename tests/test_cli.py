import sys

import pytest

from trigrams.cli import main


@pytest.fixture()
def setup_tmpdir(tmpdir):
    with tmpdir.as_cwd():
        yield


@pytest.mark.usefixtures("setup_tmpdir")
def test_cli(monkeypatch, capsys):
    with open("test_file", "w") as fout:
        fout.write("I wish I may I wish I might")
    monkeypatch.setattr(sys, "argv", ["script_name", "-i", "test_file"])
    main()
    captured_output = capsys.readouterr()
    assert "I wish => ['I', 'I']\nwish I => ['may', 'might']" in captured_output.out


@pytest.mark.usefixtures("setup_tmpdir")
def test_cli_split_data(monkeypatch, capsys):
    with open("test_file", "w") as fout:
        fout.write("I wish I may\nI wish I might")
    monkeypatch.setattr(sys, "argv", ["script_name", "-i", "test_file"])
    main()
    captured_output = capsys.readouterr()
    assert "mayI" not in captured_output.out


@pytest.mark.script_launch_mode("subprocess")
def test_run_console_script(script_runner):
    ret = script_runner.run("trigram", "--help")
    assert ret.success
