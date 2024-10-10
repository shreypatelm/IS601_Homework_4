from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        print("Exiting the program...")
        raise SystemExit  # This will terminate the application

