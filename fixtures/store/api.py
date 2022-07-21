from requests import Response
from swagger_coverage.src.deco import swagger

from fixtures.store.model import StoreResponse
from fixtures.validator import Validator


class Store(Validator):
    def __init__(self, app):
        self.app = app

    POST_STORE = "/store/{}"
    GET_STORE = "/store/{}"

    @swagger("storeAdd")
    def add_store(
        self, name: str, header=None, type_response=StoreResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_STORE.format(name)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    @swagger("storeGet")
    def get_store(
        self, name: str, header=None, type_response=StoreResponse
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_STORE.format(name)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)