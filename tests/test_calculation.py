"""
This module provides arithmetic operations using the Decimal type for 
high precision calculations, suitable for accurate numeric applications.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, division

@pytest.mark.parametrize("operand1, operand2, operation, expected", [
    (Decimal('15'), Decimal('3'), add, Decimal('18')),
    (Decimal('15'), Decimal('3'), subtract, Decimal('12')),
    (Decimal('15'), Decimal('3'), multiply, Decimal('45')),
    (Decimal('15'), Decimal('3'), division, Decimal('5')),
    (Decimal('15.5'), Decimal('3.5'), add, Decimal('19.0')),
    (Decimal('15.5'), Decimal('3.5'), subtract, Decimal('12.0')),
    (Decimal('15.5'), Decimal('3'), multiply, Decimal('46.5')),
    (Decimal('15'), Decimal('0.5'), division, Decimal('30')),
])

def test_calculation_operations(operand1, operand2, operation, expected):
    """
    Validate the perform method of the Calculation class for specified operations.

    This function asserts that the result of the calculation matches the expected 
    value for given operands and operation, helping to ensure accuracy in arithmetic operations.
    """
    calc = Calculation(operand1, operand2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {operand1} and {operand2}"


def test_calculation_repr():
    """
    Validate the __repr__ method of the Calculation class.

    This test checks if the string representation of a Calculation instance correctly 
    reflects its operands and the operation being performed, ensuring accurate object 
    representation for debugging and logging purposes.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."


def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), division)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
