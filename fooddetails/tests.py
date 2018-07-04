from django.urls import resolve
from django.test import TestCase
from fooddetails.views import homepage
from fooddetails.models import Food

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #
        self.assertEqual(found.func, homepage)

    def test_can_save_a_POST_request(self):
        # Add table in test database
        response = self.client.post('/addFooddetail', data={
        'nameFood': 'กระเพาไก่', 'volumeSugar': 5, 'volumeProtein':24})

        self.assertEqual(Food.objects.count(), 1)
        new_item = Food.objects.first()

        self.assertEqual(new_item.food_text, 'กระเพาไก่')
        self.assertEqual(new_item.sugar, 5)
        self.assertEqual(new_item.protein, 24)

    def test_can_delete_with_a_POST_request(self):
        response = self.client.post('/addFooddetail', data={
        'nameFood': 'กระเพาไก่', 'volumeSugar': 5, 'volumeProtein':24})

        self.assertEqual(Food.objects.count(), 1)

        response = self.client.post('/deleteFood', data={'food_del': 'กระเพาไก่'})
        new_item = Food.objects.first()
        self.assertEqual(Food.objects.count(), 0)
        self.assertIsNone(new_item)

    def test_can_edit_with_a_POST_request(self):
        response = self.client.post('/addFooddetail', data={
        'nameFood': 'กระเพาไก่', 'volumeSugar': 5, 'volumeProtein':24})

        self.assertEqual(Food.objects.count(), 1)
        new_item = Food.objects.first()

        self.assertEqual(new_item.food_text, 'กระเพาไก่')
        self.assertEqual(new_item.sugar, 5)
        self.assertEqual(new_item.protein, 24)

        response = self.client.post('/editFooddetail', data={
        'old_name_food': 'กระเพาไก่', 'new_name_food': 'ก๋วยเตี๋ยว', 'new_name_sugar':6, 'new_name_protein':27})

        self.assertEqual(Food.objects.count(), 1)
        new_item = Food.objects.first()

        self.assertEqual(new_item.food_text, 'ก๋วยเตี๋ยว')
        self.assertEqual(new_item.sugar, 6)
        self.assertEqual(new_item.protein, 27)
