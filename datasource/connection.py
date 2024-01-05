from enum import Enum
from typing import Protocol, runtime_checkable

from requests import Response, Session


class ConnType(Enum):
    REST = 'rest'
    GRAPHQL = 'graphql'

    def __repr__(self) -> str:
       return f"{self.value}"

@runtime_checkable
class Connection(Protocol):

    def __init__(self, bearer_token: str) -> None:
        ...
    
    def prepare_session(self, url: str) -> Response:
       ...

    def make_request(self) -> Response:
       ...

class GraphqlConnection:

    def __init__(self, method: str, route: str, bearer_token: str) -> None:
        self._bearer_token = bearer_token
        self._method = method
        self._route = route

        self._headers = {'Authorization': f'Bearer {self._bearer_token}'}

        self._session = Session()

    def prepare_session(self, url: str) -> Response:
    
        with self._session.request(
            self._method, url + self._route, headers=self._headers
        ) as response:
 
            return response
        

    def make_request(self) -> Response:
        '''What type of request; RESTful or graphQL'''
        pass
