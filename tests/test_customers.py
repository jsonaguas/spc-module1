from app import create_app
from app.models import db, Customer
import unittest
from app.utils.util import encode_token

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        self.customer = Customer(name="test_user", email="test@gmail.com", phone="1234567890", password="mypassword")
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.customer)
            db.session.commit()
        self.client = self.app.test_client()

    def test_create_customer(self):
        customer_payload = {
            "name": "John Doe",
            "email": "jdoe@gmail.com",
            "phone": "1234567890",
            "password": "mypassword"
        }
        response = self.client.post("/customers/", json=customer_payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "John Doe")

    def test_invalid_creation(self):
        customer_payload = {
            "name": "John Doe",
            "email": "jdoe@gmail.com",
            "phone": "1234567890"
        }
        response = self.client.post("/customers/", json=customer_payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"password": ["Missing data for required field."]})
    
    def test_login_customer(self):
        credentials = {
            "email":"test@gmail.com",
            "password":"mypassword"
        }
        response = self.client.post("/customers/login", json=credentials)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], "success")
        return response.json['token']

    def test_invalid_login(self):
        credentials = {
            "email":"badtest@gmail.com",
            "password":"badpassword"
        }
        response = self.client.post("/customers/login", json=credentials)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "Invalid email or password"})

    def test_update_customer(self):
        update_payload = {
            "name": "Jimmy Doe",
            "email":"jimmy@gmail.com",
            "phone":"1234567890",
            "password":"newpassword"
        }
        token = self.test_login_customer()
        print(f"Token: {token}")
        headers = {"Authorization": f"Bearer {token}"}
        # headers = {'Authorization': "Bearer" + self.test_login_customer()}
        response = self.client.put("/customers/", json=update_payload, headers=headers)
        self.assertEqual(response.status_code, 200)
