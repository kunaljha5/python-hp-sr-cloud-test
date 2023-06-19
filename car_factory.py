from dataclasses import dataclass
from enum import Enum
from typing import List, Union

ConfigurationSchema = List[Union[str, int, int, int]]

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


def validate_configuration(configuration: ConfigurationSchema) -> bool:
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


def validate_truck_configuration(params: List[Union[str, int]]) -> bool:
    engine_cylinders, wheels, doors = params

    if engine_cylinders not in [4, 6, 8]:
        return False

    if wheels != Wheels.FOUR.value:
        return False

    if doors != Doors.FOUR.value:
        return False

    return True


def validate_car_configuration(params: List[Union[str, int]]) -> bool:
    engine_cylinders, wheels, doors = params

    if engine_cylinders not in [4, 6]:
        return False

    if wheels != Wheels.FOUR.value:
        return False

    if doors == Doors.ZERO.value:
        return False

    return True


def validate_scooter_configuration(params: List[Union[str, int]]) -> bool:
    """
    :param params:
    :return: boolean
    """
    engine_cylinders, wheels, doors = params

    if engine_cylinders not in [1, 2, 3]:
        return False

    if wheels != Wheels.TWO.value:
        return False

    if doors != Doors.ZERO.value:
        return False

    return True


def validate_motorcycle_configuration(params: List[Union[str, int]]) -> bool:
    """
    :param params:
    :return: boolean
    """
    engine_cylinders, wheels, doors = params

    if engine_cylinders not in [2, 4]:
        return False
    if wheels != Wheels.ONE.value:
        return False
    if doors != Doors.ZERO.value:
        return False
    return True
