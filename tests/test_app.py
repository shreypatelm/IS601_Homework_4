import pytest
from app import App

@pytest.mark.parametrize("command", [
    ('add'),
    ('subtract'),
    ('multiply'),
    ('divide'),
])
def test_calculation_operations(command, monkeypatch):
    """Simulate command followed by exit."""
    inputs = iter([f'{command} 1 1', 'exit'])  # Simulate command with arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    
    with pytest.raises(SystemExit) as e:
        app.start()  # Ensure the app start triggers SystemExit
    
    assert e.type == SystemExit  # Check if SystemExit was raised
    assert str(e.value) == "Exiting..."  # Ensure correct exit message

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "Available commands: add, subtract, multiply, divide, exit","Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit." in captured.out
    assert "Exiting the program..." in captured.out

def test_app_invalid_input_format(capfd, monkeypatch):
    """Test how the REPL handles invalid input formats."""
    # Simulate invalid input followed by 'exit'
    inputs = iter(['add 2', 'exit'])  # Missing one argument for 'add'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Verify that the invalid input format was handled as expected
    captured = capfd.readouterr()
    assert "Invalid input format. Please enter command followed by two numbers." in captured.out
    assert "Exiting the program..." in captured.out
