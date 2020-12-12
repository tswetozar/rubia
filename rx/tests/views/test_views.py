from django.contrib.auth import authenticate
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUser


class WorkflowViewsTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getWorkflowPage_ShouldRenderCorrectTemplate(self):
        response = self.test_client.get(reverse('current user profile'))
        self.assertTemplateUsed(response, 'registration/user_workflow.html')
        rxs = response.context['rxs']
        self.assertEqual(0, len(rxs))
        form = response.context['form']
        self.assertIsNotNone(form)

    def test_postCreateRxWorkflowPage_ShouldRedirectsCorrectly(self):
        first_name = 'Ivan'
        last_name = 'Draganov'
        age = '57'
        user = CustomUser(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        user.save()
        new_photo_image = SimpleUploadedFile(name='image_file_for_testing.jpg',
                                             content=open('media/public/rx/image_file_for_testing.jpg', 'rb').read(),
                                             content_type='image/jpeg')

        data = {
            'age': age,
            'last_name': last_name,
            'first_name': first_name,
            'image': new_photo_image,
        }
        self.test_client.login(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        response = self.test_client.post(reverse('create rx'), data=data)
        self.assertRedirects(reverse('current user profile'))


