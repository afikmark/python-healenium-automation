from retrying import retry
from functools import partial

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
