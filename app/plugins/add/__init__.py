from app.commands import Command

class AddCommand(Command):
    def execute(self, a: float, b: float) -> str:
        return f"The answer is {a + b}"


