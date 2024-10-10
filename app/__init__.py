from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here (command name mapped to command class)
        self.command_handler.register_command("add", AddCommand)
        self.command_handler.register_command("subtract", SubtractCommand)
        self.command_handler.register_command("multiply", MultiplyCommand)
        self.command_handler.register_command("divide", DivideCommand)
        self.command_handler.register_command("exit", ExitCommand)

        print("Available commands: add, subtract, multiply, divide, exit")
        print("Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit.")

        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                self.command_handler.execute_command("exit")
                break

            # Parse user input into command and arguments
            try:
                command_name, a, b = user_input.split()
                a = float(a)
                b = float(b)
                self.command_handler.execute_command(command_name, a, b)
            except ValueError:
                print("Invalid input format. Please enter command followed by two numbers.")
            except KeyError:
                print(f"No such command: {command_name}")
