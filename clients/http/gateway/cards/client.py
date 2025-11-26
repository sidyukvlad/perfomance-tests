from clients.http.client import HTTPClient, Response
from typing import TypedDict


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной карты.
    """
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для выпуска физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """
    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Создание виртуальной карты.

        :param request: Словарь с данными виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card")

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Создание физической карты.

        :param request: Словарь с данными физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card")