from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()
class PostAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='test', email='test@test.com')
        user.set_password("123456789")
        user.save()

        post = Post.objects.create(
            title = 'Covoiturage pour le terre',
            an_type =  1,
            price = '10',
            content = 'rpovopez,vopz,vop,oez,o,',
            num_street = '19',
            street = 'Leon Gambetta',
            city = 'Belfort',
            postalcode = '90000',
            country = 'France',
            category = 2,
            author = 2,
        )

        def test_single_user(self):
            user_count = User.objects.count()
            self.assertEqual(user_count, 1)

        def test_single_post(self):
            post_count = Post.objects.count()
            self.assertEqual(post_count, 1)