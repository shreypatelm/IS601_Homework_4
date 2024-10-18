import logging
from app.commands import Command

class SubtractCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a - b

    def execute(self, *args, **kwargs):
        a, b = map(float, args)  # Convert inputs to float
        logging.info(f'{a} - {b} = {self.evaluate(a, b)}')
        print(f'{a} - {b} = {self.evaluate(a, b)}')

# import logging
# from app.commands import Command

# class SubtractCommand(Command):
#     @staticmethod
#     def evaluate(a: float, b: float) -> float:
#         return a - b

#     def execute(self, *args, **kwargs):
#         a, b = args[0]
#         res = f'{a} - {b} = {self.evaluate(a,b)}'
#         logging.info(f'Performed substraction operation --> {res}'); print(res)