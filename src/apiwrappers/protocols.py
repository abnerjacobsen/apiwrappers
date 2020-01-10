from apiwrappers.compat import Protocol
from apiwrappers.entities import Request, Response
from apiwrappers.typedefs import Timeout


class Driver(Protocol):
    timeout: Timeout
    verify_ssl: bool

    def fetch(self, request: Request) -> Response:
        ...


class AsyncDriver(Protocol):
    timeout: Timeout
    verify_ssl: bool

    async def fetch(self, request: Request) -> Response:
        ...
