from requests import Response
from swagger_coverage.src.deco import swagger

from fixtures.auth.model import AuthResponse, Auth
from fixtures.validator import Validator


class AuthUser(Validator):
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    @swagger("authUser")
    def login(self, data: Auth, type_response=AuthResponse) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.to_dict(),
        )
        return self.structure(response, type_response=type_response)
