from dataclasses import dataclass
from enum import Enum


@dataclass
class EngineCylinders:
    value: int


@dataclass
class Wheels(Enum):
    FOUR = 4
    TWO = 2
    ONE = 1


@dataclass
class Doors(Enum):
    TWO = 2
    FOUR = 4
    ZERO = 0


def validate_configuration(configuration):
    vehicle_type = configuration[0]
    params = configuration[1:]

    if vehicle_type == "Truck":
        return validate_truck_configuration(params)
    elif vehicle_type == "Car":
        return validate_car_configuration(params)
    elif vehicle_type == "Scooter":
        return validate_scooter_configuration(params)
    elif vehicle_type == "Motorcycle":
        return validate_motorcycle_configuration(params)
    else:
        raise ValueError("Invalid vehicle type")


def validate_truck_configuration(params):
    engine_cylinders, wheels, doors = params

    if not isinstance(
        engine_cylinders, EngineCylinders
    ) or engine_cylinders.value not in [4, 6, 8]:
        return False

    if wheels is not Wheels.FOUR:
        return False

    if doors is not Doors.FOUR:
        return False

    return True


def validate_car_configuration(params):
    engine_cylinders, wheels, doors = params

    if not isinstance(
        engine_cylinders, EngineCylinders
    ) or engine_cylinders.value not in [4, 6]:
        return False

    if wheels is not Wheels.FOUR:
        return False

    if doors is Doors.ZERO:
        return False

    return True


def validate_scooter_configuration(params):
    """
    :param params:
    :return: boolean
    """
    engine_cylinders, wheels, doors = params

    if not isinstance(
        engine_cylinders, EngineCylinders
    ) or engine_cylinders.value not in [1, 2, 3]:
        return False

    if wheels is not Wheels.TWO:
        return False

    if doors is not Doors.ZERO:
        return False

    return True


def validate_motorcycle_configuration(params):
    """
    :param params:
    :return: boolean
    """
    engine_cylinders, wheels, doors = params

    if not isinstance(
        engine_cylinders, EngineCylinders
    ) or engine_cylinders.value not in [2, 4]:
        return False
    if wheels is not Wheels.ONE:
        return False
    if doors is not Doors.ZERO:
        return False
    return True
