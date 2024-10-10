# from app.commands import CommandHandler
# from app.plugins.add import AddCommand
# from app.plugins.subtract import SubtractCommand
# from app.plugins.multiply import MultiplyCommand
# from app.plugins.divide import DivideCommand
# from app.plugins.exit import ExitCommand

# class App:
#     def __init__(self):  # Constructor
#         self.command_handler = CommandHandler()

#     def start(self):
#         # Register commands here (command name mapped to command class)
#         self.command_handler.register_command("add", AddCommand)
#         self.command_handler.register_command("subtract", SubtractCommand)
#         self.command_handler.register_command("multiply", MultiplyCommand)
#         self.command_handler.register_command("divide", DivideCommand)
#         self.command_handler.register_command("exit", ExitCommand)

#         print("Available commands: add, subtract, multiply, divide, exit")
#         print("Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit.")

#         while True:  # REPL (Read, Evaluate, Print, Loop)
#             user_input = input(">>> ").strip().lower()
#             if user_input == "exit":
#                 self.command_handler.execute_command("exit")
#                 break

#             # Parse user input into command and arguments
#             try:
#                 command_name, a, b = user_input.split()
#                 a = float(a)
#                 b = float(b)
#                 self.command_handler.execute_command(command_name, a, b)
#             except ValueError:
#                 print("Invalid input format. Please enter command followed by two numbers.")
#             except KeyError:
#                 print(f"No such command: {command_name}")
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command  # Ensure to import the base Command class

class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        # Iterate over all modules in the plugins package
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                # Iterate over all items in the module
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        # Check if the item is a subclass of Command
                        if issubclass(item, Command):  
                            # Register the command with its name (plugin_name) and create an instance
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        # Load all plugins dynamically
        self.load_plugins()
        print("Available commands: ", ', '.join(self.command_handler.commands.keys()))
        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                self.command_handler.execute_command("exit")
                break

            try:
                command_name, a, b = user_input.split()
                a = float(a)
                b = float(b)
                result = self.command_handler.execute_command(command_name, a, b)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input format. Please enter command followed by two numbers.")
            except KeyError:
                print(f"No such command: {command_name}. Available commands are: {', '.join(self.command_handler.commands.keys())}.")
