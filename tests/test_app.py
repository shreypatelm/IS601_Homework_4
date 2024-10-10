import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

# def test_app_start_unknown_command(capfd, monkeypatch):
#     """Test how the REPL handles an unknown command before exiting."""
#     # Simulate user entering an unknown command followed by 'exit'
#     inputs = iter(['unknown_command', 'exit'])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))

#     app = App()

#     with pytest.raises(SystemExit) as excinfo:
#         app.start()

#     # Verify that the unknown command was handled as expected
#     captured = capfd.readouterr()
#     assert "No such command: unknown_command" in captured.out
#     assert "Exiting the program..." in captured.out

# def test_app_invalid_input_format(capfd, monkeypatch):
#     """Test how the REPL handles invalid input formats."""
#     # Simulate invalid input followed by 'exit'
#     inputs = iter(['add 2', 'exit'])  # Missing one argument for 'add'
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))

#     app = App()

#     with pytest.raises(SystemExit) as excinfo:
#         app.start()

#     # Verify that the invalid input format was handled as expected
#     captured = capfd.readouterr()
#     assert "Invalid input format. Please enter command followed by two numbers." in captured.out
#     assert "Exiting the program..." in captured.out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
