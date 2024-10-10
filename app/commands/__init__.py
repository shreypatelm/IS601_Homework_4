from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        """Execute the command with the provided arguments."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        """Register a command with its corresponding name."""
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        """ 
        Execute the command by its name, passing any arguments.
        command_name: The name of the command (e.g., 'add', 'subtract')
        *args: The extra arguments for the command (e.g., numbers a and b)
        """
        if command_name not in self.commands:
            print(f"No such command: {command_name}")
            return

        command_class = self.commands[command_name]  # Get the command class
        command_instance = command_class()  # Create a new instance of the command
        
        return command_instance.execute(*args)  # Execute the command with arguments
