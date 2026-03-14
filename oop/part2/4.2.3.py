from dataclasses import dataclass


@dataclass(frozen=True)
class APIConfig:
    base_url: str
    api_key: str
