import unittest
from app import create_app

class DashboardTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_dashboard_load(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Real-Time Monitoring', response.data)

    def test_historical_load(self):
        response = self.client.get('/historical')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Historical Analysis', response.data)

    def test_control_load(self):
        response = self.client.get('/control')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bot Control Center', response.data)

    def test_system_load(self):
        response = self.client.get('/system')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'System Management', response.data)

if __name__ == '__main__':
    unittest.main()