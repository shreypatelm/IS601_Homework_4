"""
This module provides a pytest-based test framework for testing calculator operations.
It dynamically generates test data using Faker for the `add`, `subtract`, `multiply`, and `division` operations,
and handles cases like division by zero. Test cases can be parameterized with a custom number of records.
"""
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, division

fake = Faker()

def generate_test_data(num_records):
    """
    Generates test data for calculator operations, yielding operands and expected results.

    Parameters:
        num_records (int): Number of test records to generate.
    """
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': division
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func is division:
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func is division and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected


def pytest_addoption(parser):
    """
    Adds a pytest command-line option for specifying the number of test records.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")


def pytest_generate_tests(metafunc):
    """
    Generates test parameters based on dynamic fixtures and the specified number of records.
    """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
