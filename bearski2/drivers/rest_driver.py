"""REST API 驱动"""
import requests

class RESTDriver:
    def __init__(self, session):
        self.session = session
        if not self.session.rest_session:
            self.session.rest_session = requests.Session()
    
    def get(self, url, **kwargs):
        response = self.session.rest_session.get(url, **kwargs)
        return response
    
    def post(self, url, **kwargs):
        response = self.session.rest_session.post(url, **kwargs)
        return response
    
    def assert_status(self, response, expected):
        assert response.status_code == expected
