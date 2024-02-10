from enum import Enum


class Timeout(Enum):
    SHORT_ELEMENT_WAIT = 10
    MEDIUM_ELEMENT_WAIT = 30
    LONG_ELEMENT_WAIT = 40


EXPECTED_NUMBER_OF_PRODUCTS_PER_PAGE = {
    'laptops': 6,
    'phones': 7,
    'monitors': 2
}

