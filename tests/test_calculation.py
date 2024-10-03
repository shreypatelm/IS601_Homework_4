"""
This module contains tests for the calculator operations and Calculation class.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, division

# pylint: disable=invalid-name
def test_calculation_operations(a, b, operation, expected):
    """
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Tests the __repr__ method of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    # assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."
    assert repr(calc) == expected_repr, "The repr method output does not match the expected string."

def test_divide_by_zero():
    """
    Tests that dividing by zero raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), division)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
