class ApiError(Exception):
    pass


class AuthError(ApiError):
    pass


class TimeoutError(ApiError):
    pass


def make_request(should_fail_with: str) -> None:
    if should_fail_with == "auth":
        raise AuthError
    if should_fail_with == "timeout":
        raise TimeoutError
