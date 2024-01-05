from datasource.connection import Connection, GraphqlConnection
from datasource.datasource import GraphqlDataSource


def main() -> None:
    test = GraphqlConnection(method='GET', route='/bearer', bearer_token='password123')
    conn = GraphqlDataSource(url='https://httpbin.org')
    r = conn.make_connection(test)
    print(f'r.json(): {r.json()}')
    print(f'type(test): {type(test)}')
    print(f'isinstance(test, Connection): {isinstance(test, Connection)}')


if __name__ == "__main__":
    main()
