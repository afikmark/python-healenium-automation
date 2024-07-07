from requests import Session, request, Response


class RestApi:

    def __init__(self, url, session: Session):
        self.url = url
        self.session = session

    def _api_call(self, method, url, *args, **kwargs) -> Response:
        response = self.session.request(method, url, *args, **kwargs)
        response.raise_for_status()
        return response

    def get(self, url, *args, **kwargs) -> Response:
        return self._api_call('get', url, *args, **kwargs)

    def post(self, url, *args, **kwargs) -> Response:
        return self._api_call('post', url, *args, **kwargs)

    def patch(self, url, *args, **kwargs) -> Response:
        return self._api_call('patch', url, *args, **kwargs)

    def put(self, url, *args, **kwargs) -> Response:
        return self._api_call('put', url, *args, **kwargs)

    def delete(self, url, *args, **kwargs) -> Response:
        return self._api_call('delete', url, *args, **kwargs)
