from typing import Protocol, runtime_checkable

from requests import Response

from datasource.connection import Connection


@runtime_checkable
class DataSource(Protocol):

    def __init__(self, url: str) -> None:
        ...

    def make_connection(self, conn: Connection) -> Response:
        ...



class GraphqlDataSource:

    def __init__(self, url: str) -> None:
        self._url = url

    def make_connection(self, conn: Connection) -> Response:
        return conn.prepare_session(self._url)
    