from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import CustomUser
from common.models import OffensiveWord
from rx.forms import CreateRxForm
from rx.models import Rx


class TestRxCreateForm(TestCase):
    def test_form_whenValidName_shouldBeValid(self):
        first_name = 'Ivan'
        last_name = 'Draganov'
        age = '57'
        user = CustomUser(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        user.save()
        new_photo_image = SimpleUploadedFile(name='image_file_for_testing.jpg',
                                             content=open('media/public/rx/image_file_for_testing.jpg', 'rb').read(),
                                             content_type='image/jpeg')
        form = CreateRxForm(data={
            'age': age,
            'last_name': last_name,
            'first_name': first_name,
        },
            files={
                'image': new_photo_image
            })

        self.assertTrue(form.is_valid())

    def test_form_whenNameContainsNumber_shouldRaise(self):
        first_name = 'Ivan3'
        last_name = 'Draganov'
        age = '57'
        user = CustomUser(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        user.save()
        new_photo_image = SimpleUploadedFile(name='image_file_for_testing.jpg',
                                             content=open('media/public/rx/image_file_for_testing.jpg', 'rb').read(),
                                             content_type='image/jpeg')
        form = CreateRxForm(
            data={
                'age': age,
                'last_name': last_name,
                'first_name': first_name,
            },
            files={
                'image': new_photo_image
            }
        )

        self.assertFalse(form.full_clean())

    def test_createRx_whenNameContainsBadLanguage_shouldRaise(self):
        first_name = '1234'
        last_name = 'Draganov'
        age = '57'
        user = CustomUser(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        user.save()
        new_photo_image = SimpleUploadedFile(name='image_file_for_testing.jpg',
                                             content=open('media/public/rx/image_file_for_testing.jpg', 'rb').read(),
                                             content_type='image/jpeg')

        bad_words_collection = ['qwer', 'asdf', 'bloody', 'zxcv']
        for word in bad_words_collection:
            item = OffensiveWord(word=word)
            item.save()

        form = CreateRxForm(
            data={
                'age': age,
                'last_name': last_name,
                'first_name': first_name,
            },
            files={
                'image': new_photo_image
            }
        )

        self.assertFalse(form.full_clean())
