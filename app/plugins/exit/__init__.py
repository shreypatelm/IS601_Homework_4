import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args, **kwargs):
        sys.exit("Exiting the program...")

# import sys
# from app.commands import Command

# class ExitCommand(Command):
#     def execute(self, *args, **kwargs):
#         sys.exit("Exiting...")
        