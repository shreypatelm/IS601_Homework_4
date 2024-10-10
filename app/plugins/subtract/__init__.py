from app.commands import Command

class SubtractCommand(Command):
    def execute(self, a, b):
        print(f"The answer is {a - b}")