from http import HTTPStatus

from fastapi.testclient import TestClient

from dev_sm.app import app


def test_root_deve_retornar_hello_world():
    """
    Esse teste tem 3 etapas (AAA)
    - Arrange
    - Act
    - Assert
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello world!'}
    assert response.status_code == HTTPStatus.OK
