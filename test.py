from car_factory import (
    EngineCylinders,
    Wheels,
    Doors,
    validate_configuration,
)
import pytest


def test_valid_truck_configuration():
    configuration = ["Truck", EngineCylinders(6), Wheels.FOUR, Doors.FOUR]
    assert validate_configuration(configuration) is True


def test_invalid_truck_configuration():
    configuration = ["Truck", EngineCylinders(1), Wheels.FOUR, Doors.FOUR]
    assert validate_configuration(configuration) is False


def test_invalid_truck_1_configuration():
    configuration = ["Truck", EngineCylinders(6), Wheels.TWO, Doors.FOUR]
    assert validate_configuration(configuration) is False


def test_invalid_truck_2_configuration():
    configuration = ["Truck", EngineCylinders(6), Wheels.FOUR, Doors.TWO]
    assert validate_configuration(configuration) is False


def test_valid_car_configuration():
    configuration = ["Car", EngineCylinders(4), Wheels.FOUR, Doors.TWO]
    assert validate_configuration(configuration) is True


def test_invalid_car_configuration():
    configuration = ["Car", EngineCylinders(8), Wheels.FOUR, Doors.ZERO]
    assert validate_configuration(configuration) is False


def test_invalid_car_1_configuration():
    configuration = ["Car", EngineCylinders(4), Wheels.TWO, Doors.TWO]
    assert validate_configuration(configuration) is False


def test_invalid_car_2_configuration():
    configuration = ["Car", EngineCylinders(4), Wheels.FOUR, Doors.ZERO]
    assert validate_configuration(configuration) is False


def test_valid_scooter_configuration():
    configuration = ["Scooter", EngineCylinders(1), Wheels.TWO, Doors.ZERO]
    assert validate_configuration(configuration) is True


def test_invalid_scooter_configuration():
    configuration = ["Scooter", EngineCylinders(3), Wheels.TWO, Doors.FOUR]
    assert validate_configuration(configuration) is False


def test_invalid_scooter_1_configuration():
    configuration = ["Scooter", EngineCylinders(6), Wheels.TWO, Doors.FOUR]
    assert validate_configuration(configuration) is False


def test_invalid_scooter_2_configuration():
    configuration = ["Scooter", EngineCylinders(3), Wheels.FOUR, Doors.FOUR]
    assert validate_configuration(configuration) is False


def test_valid_motorcycle_configuration():
    configuration = ["Motorcycle", EngineCylinders(4), Wheels.ONE, Doors.ZERO]
    assert validate_configuration(configuration) is True


def test_invalid_motorcycle_configuration():
    configuration = ["Motorcycle", EngineCylinders(6), Wheels.ONE, Doors.TWO]
    assert validate_configuration(configuration) is False


def test_invalid_motorcycle_1_configuration():
    configuration = ["Motorcycle", EngineCylinders(2), Wheels.TWO, Doors.TWO]
    assert validate_configuration(configuration) is False


def test_invalid_motorcycle_2_configuration():
    configuration = ["Motorcycle", EngineCylinders(2), Wheels.ONE, Doors.FOUR]
    assert validate_configuration(configuration) is False


def test_invalid_vehicle_configuration():
    configuration = ["F1", EngineCylinders(6), Wheels.ONE, Doors.TWO]
    with pytest.raises(ValueError) as error:
        validate_configuration(configuration)
    assert str(error.value) == "Invalid vehicle type"
