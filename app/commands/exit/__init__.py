import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args):
        print("Exiting the program...")
        sys.exit(0)  # Gracefully exit the program
