from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()
#dyamic function
def create_user(**params):
    """create new user"""
    return get_user_model().objects.create_user(**params)

class UserTestCase(TestCase):
    def setUp(self):
        self.user = create_user(
            email='test@gmail.com',
            username='test',
            password='testpass',
        )

    def test_created_user(self):
        qs = User.objects.filter(username='test')
        self.assertEqual(qs.count(), 1)