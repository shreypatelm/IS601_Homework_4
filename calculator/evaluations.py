from typing import List

from calculator.calculation import Calculation

class Evaluations:
    history:List[Calculation] = []

    @classmethod
    def add_calculation(cls, evaluation: Calculation):
        """Added a calculation to the history."""
        cls.history.append(evaluation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there is no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
