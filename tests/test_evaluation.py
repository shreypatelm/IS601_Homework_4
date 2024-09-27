'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.evaluations import Evaluations
from calculator.operations import add, subtract


@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Evaluations.clear_history()
    Evaluations.add_calculation(Calculation(Decimal('10'), Decimal('15'), add))
    Evaluations.add_calculation(Calculation(Decimal('30'), Decimal('5'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Evaluations.add_calculation(calc)
    assert Evaluations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Evaluations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Evaluations.clear_history()
    assert len(Evaluations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Evaluations.get_latest()
    assert latest.a == Decimal('30') and latest.b == Decimal('5'), "Did not get latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Evaluations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct no of calculations with add op."
    subtract_operations = Evaluations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct no of calculations with subtract op."

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Evaluations.clear_history()
    assert Evaluations.get_latest() is None, "Expected None for latest calculation with empty history"
    