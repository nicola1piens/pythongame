import unittest
import json
from app import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_pokemon(self):
        response = self.client.get('/pokemon/1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Bulbasaur')
        self.assertEqual(data['type'], ['Grass', 'Poison'])
        self.assertEqual(data['hp'], 45)

    def test_get_invalid_pokemon(self):
        response = self.client.get('/pokemon/999')
        self.assertEqual(response.status_code, 404)

    def test_create_pokemon(self):
        data = {'name': 'Test', 'type': ['Test'], 'hp': 50}
        response = self.client.post(
            '/pokemon', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_invalid_pokemon(self):
        data = {'name': 'Test', 'type': ['Test']}
        response = self.client.post(
            '/pokemon', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
