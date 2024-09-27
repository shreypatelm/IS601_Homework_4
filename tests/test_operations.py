'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, division


def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('24'), Decimal('4'), add)
    assert calculation.perform() == Decimal('28'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('24'), Decimal('4'), subtract)
    assert calculation.perform() == Decimal('20'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('24'), Decimal('4'), multiply)
    assert calculation.perform() == Decimal('96'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('24'), Decimal('4'), division)
    assert calculation.perform() == Decimal('6'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('24'), Decimal('0'), division)
        calculation.perform()
        