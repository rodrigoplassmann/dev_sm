from http import HTTPStatus

from fastapi import FastAPI

from dev_sm.schemas import Message

app = FastAPI(title='Dev Social Media')


@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def read_root():
    return {'message': 'Hello world!'}
