from car_factory import (
    EngineCylinders,
    Wheels,
    Doors,
    validate_configuration,
)
from pytest import raises
from typing import List, Union

ConfigurationSchema = List[Union[str, int, int, int]]


def test_valid_truck_configuration() -> None:
    configuration: ConfigurationSchema = ["Truck", 6, 4, 4]
    assert validate_configuration(configuration) is True


def test_invalid_truck_configuration() -> None:
    configuration: ConfigurationSchema = ["Truck", 1, 4, 4]
    assert validate_configuration(configuration) is False


def test_invalid_truck_1_configuration() -> None:
    configuration: ConfigurationSchema = ["Truck", 6, 2, 4]
    assert validate_configuration(configuration) is False


def test_invalid_truck_2_configuration() -> None:
    configuration: ConfigurationSchema = ["Truck", 6, 4, 2]
    assert validate_configuration(configuration) is False


def test_valid_car_configuration() -> None:
    configuration: ConfigurationSchema = ["Car", 4, 4, 2]
    assert validate_configuration(configuration) is True


def test_invalid_car_configuration() -> None:
    configuration: ConfigurationSchema = ["Car", 8, 4, 0]
    assert validate_configuration(configuration) is False


def test_invalid_car_1_configuration() -> None:
    configuration: ConfigurationSchema = ["Car", 4, 2, 4]
    assert validate_configuration(configuration) is False


def test_invalid_car_2_configuration() -> None:
    configuration: ConfigurationSchema = ["Car", 4, 4, 0]
    assert validate_configuration(configuration) is False


def test_valid_scooter_configuration() -> None:
    configuration: ConfigurationSchema = ["Scooter", 1, 2, 0]
    assert validate_configuration(configuration) is True


def test_invalid_scooter_configuration() -> None:
    configuration: ConfigurationSchema = ["Scooter", 3, 2, 4]
    assert validate_configuration(configuration) is False


def test_invalid_scooter_1_configuration() -> None:
    configuration: ConfigurationSchema = [
        "Scooter",
        str(EngineCylinders(6)),
        str(Wheels.TWO.value),
        str(Doors.FOUR.value),
    ]
    assert validate_configuration(configuration) is False


def test_invalid_scooter_2_configuration() -> None:
    configuration: ConfigurationSchema = ["Scooter", 3, 4, 4]
    assert validate_configuration(configuration) is False


def test_valid_motorcycle_configuration() -> None:
    configuration: ConfigurationSchema = ["Motorcycle", 4, 1, 0]
    assert validate_configuration(configuration) is True


def test_invalid_motorcycle_configuration() -> None:
    configuration: ConfigurationSchema = ["Motorcycle", 6, 1, 2]
    assert validate_configuration(configuration) is False


def test_invalid_motorcycle_1_configuration() -> None:
    configuration: ConfigurationSchema = ["Motorcycle", 2, 2, 2]
    assert validate_configuration(configuration) is False


def test_invalid_motorcycle_2_configuration() -> None:
    configuration: ConfigurationSchema = ["Motorcycle", 2, 1, 4]
    assert validate_configuration(configuration) is False


def test_invalid_vehicle_configuration() -> None:
    configuration: ConfigurationSchema = ["F1", 6, 1, 2]
    with raises(ValueError) as error:
        validate_configuration(configuration)
    assert str(error.value) == "Invalid vehicle type"
