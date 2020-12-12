from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import CustomUser
from common.models import OffensiveWord
from rx.models import Rx


class TestProfileModel(TestCase):
    def test_createRx_whenValidName_shouldCreateRx(self):
        first_name = 'Ivan'
        last_name = 'Draganov'
        age = '57'
        user = CustomUser(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        user.save()
        new_photo_image = SimpleUploadedFile(name='image_file_for_testing.jpg',
                                             content=open('media/public/rx/image_file_for_testing.jpg', 'rb').read(),
                                             content_type='image/jpeg')
        rx = Rx()
        rx.image = new_photo_image
        rx.user = user
        rx.age = age
        rx.last_name = last_name
        rx.first_name = first_name
        rx.full_clean()
        rx.save()

    def test_createRx_whenNameContainsDigits_shouldRaise(self):
        first_name = 'Ivan3'
        last_name = 'Draganov'
        age = '57'
        user = CustomUser(email='test@abv.bg', password='qappU6-fabmiv-fuzjev')
        user.save()
        new_photo_image = SimpleUploadedFile(name='image_file_for_testing.jpg',
                                             content=open('media/public/rx/image_file_for_testing.jpg', 'rb').read(),
                                             content_type='image/jpeg')
        with self.assertRaises(ValidationError) as context:
            rx = Rx()
            rx.image = new_photo_image
            rx.user = user
            rx.age = age
            rx.last_name = last_name
            rx.first_name = first_name
            rx.full_clean()
            rx.save()

        self.assertIsNotNone(context.exception)

    def test_createRx_whenNameContainsBadLanguage_shouldRaise(self):
        first_name = 'bloody'
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


        with self.assertRaises(ValidationError) as context:
            rx = Rx()
            rx.image = new_photo_image
            rx.user = user
            rx.age = age
            rx.last_name = last_name
            rx.first_name = first_name
            rx.full_clean()
            rx.save()

        self.assertIsNotNone(context.exception)
