from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Status

User = get_user_model()
#dyamic function
def create_user(**params):
    """create new user"""
    return get_user_model().objects.create_user(**params)

class StatusTestCase(TestCase):
    def setUp(self):
        self.user = create_user(
            email='test@gmail.com',
            username='test',
            password='testpass',
        )

    def test_creating_status(self):
        user = User.objects.get(username='test')
        obj = Status.objects.create(user=user, content="HH")
        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(),1)