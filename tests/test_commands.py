import pytest
from app import App
from app.plugins.exit import ExitCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

# Test for ExitCommand
def test_exit_command(capfd):
    command = ExitCommand()
    with pytest.raises(SystemExit):
        command.execute()
    out, err = capfd.readouterr()
    assert out == "Exiting the program...\n", "The ExitCommand should print 'Exiting the program...'"

# Test for AddCommand
def test_app_add_command(capfd, monkeypatch):
    inputs = iter(['add 2 3', 'exit'])  # Simulate input for REPL
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, err = capfd.readouterr()
    assert "The answer is 5" in out, "AddCommand should output 'The answer is 5'"
    assert "Exiting the program..." in out

# Test for SubtractCommand
def test_app_subtract_command(capfd, monkeypatch):
    inputs = iter(['subtract 5 3', 'exit'])  # Simulate input for REPL
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, err = capfd.readouterr()
    assert "The answer is 2" in out, "SubtractCommand should output 'The answer is 2'"
    assert "Exiting the program..." in out

# Test for MultiplyCommand
def test_app_multiply_command(capfd, monkeypatch):
    inputs = iter(['multiply 3 4', 'exit'])  # Simulate input for REPL
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, err = capfd.readouterr()
    assert "The answer is 12" in out, "MultiplyCommand should output 'The answer is 12'"
    assert "Exiting the program..." in out

# Test for DivideCommand
def test_app_divide_command(capfd, monkeypatch):
    inputs = iter(['divide 10 2', 'exit'])  # Simulate input for REPL
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, err = capfd.readouterr()
    assert "The answer is 5.0" in out, "DivideCommand should output 'The answer is 5.0'"
    assert "Exiting the program..." in out

# Test for divide by zero handling
def test_divide_by_zero(capfd, monkeypatch):
    inputs = iter(['divide 10 0', 'exit'])  # Simulate input for REPL
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, err = capfd.readouterr()
    assert "Cannot divide by zero!" in out, "DivideCommand should handle divide by zero case"
    assert "Exiting the program..." in out
