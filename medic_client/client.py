import requests

class MedicClient:
    def __init__(self, api_key, base_url='https://api.herbstack.com'):
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, method, endpoint, data=None):
        headers = {'X-API-Key': self.api_key}
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_symptoms(self):
        return self._make_request('GET', 'symptoms/')

    def log_symptom(self, symptom, severity):
        data = {'symptom': symptom, 'severity': severity}
        return self._make_request('POST', 'symptoms/', data)

    def get_ai_response(self, question):
        data = {'user_input': question}
        return self._make_request('POST', 'ai/chat/', data)
