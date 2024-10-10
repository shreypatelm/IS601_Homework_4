from app.commands import Command

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(f"The answer is {a / b}")

