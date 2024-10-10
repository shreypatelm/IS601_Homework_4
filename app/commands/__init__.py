from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        """ 
        command_name: The name of the command (e.g., 'add', 'subtract')
        *args: The extra arguments for the command (e.g., numbers a and b)
        """
        try:
            command_class = self.commands[command_name]
            command = command_class()  # Create a new instance of the command
            command.execute(*args)  # Pass the arguments (e.g., a and b)
        except KeyError:
            print(f"No such command: {command_name}")