from app.commands import Command

class AddCommand(Command):
    def execute(self, a, b):
        print(f"The answer is {a + b}")
