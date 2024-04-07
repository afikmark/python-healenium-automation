from retrying import retry
from functools import partial
import re

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
    retry_on_result=lambda value: value in [None, [], {}, ''],
    wrap_exception=True

)


class Regex:

    @staticmethod
    def match_all_after_prefix(prefix, text):
        return re.match(rf'{prefix}(.*)', text).group(1)
