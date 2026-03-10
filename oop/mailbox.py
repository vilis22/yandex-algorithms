from typing import Any, Optional


class Mailbox:
    def __init__(self) -> None:
        self._owner: Optional[str] = None

    def get_owner(self) -> Optional[str]:
        return self._owner

    def set_owner(self, new_owner: Any) -> None:
        if isinstance(new_owner, str):
            self._owner = new_owner
