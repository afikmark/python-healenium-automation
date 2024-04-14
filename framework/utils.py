import string
from framework.database.users_queries import UsersQueries
from retrying import retry
from functools import partial
import re
import random

DEFAULT_WAIT_TIME = 25000
DEFAULT_STOP_MAX_ATTEMPT_NUMBER = 3

retry_on_false = partial(
    retry,
    wait_fixed=1500,
    stop_max_attempt_number=5,
    retry_on_result=lambda value: value is False,
    wrap_exception=True
)

retry_on_true = partial(
    retry,
    wait_fixed=1500,
    stop_max_attempt_number=5,
    retry_on_result=lambda value: value is True,
    wrap_exception=True
)

retry_on_empty_result = partial(
    retry,
    wait_fixed=1500,
    stop_max_attempt_number=5,
    retry_on_result=lambda value: value in [None, [], {}, '']

)


class Regex:
    """Class for all regular expressions used for testing"""

    @staticmethod
    def match_all_after_prefix(prefix, text):
        return re.match(rf'{prefix}(.*)', text).group(1)


USER_QUERIES = UsersQueries()


class DataGenerator:
    """Data generator class for tests"""

    @staticmethod
    def ssn() -> str:
        """Social security number. nine-digit number issued to U.S. citizens"""

        area_number = f'{random.randint(100, 899)}'
        group_number = f'{random.choice(string.digits)}{random.choice(string.digits[1:])}'
        serial_number = ''.join(random.sample(string.digits, k=4))

        return f'{area_number}{group_number}{serial_number}'

    @staticmethod
    def first_name() -> str:
        first_names = USER_QUERIES.get_first_names()
        return random.choice(first_names)

    @staticmethod
    def last_name() -> str:
        last_names = USER_QUERIES.get_last_names()
        return random.choice(last_names)

    # @staticmethod
    # def address() -> str:
