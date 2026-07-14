from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_employees():

    query = """

    query{

        employees{

            id

            name

        }

    }

    """

    response = client.post(

        "/graphql",

        json={

            "query": query

        }

    )

    assert response.status_code == 200