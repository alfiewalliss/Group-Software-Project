from django.test import TestCase, Client

# Tests that each view is at the expected URL, returns the expected status code and uses the expected template
class TestViews(TestCase):
    
    def test_sign_up_view(self):
        url = self.client.get('/signUp')
        self.assertEqual(url.status_code, 301)
        self.assertTemplateUsed('locationgameapp/signUp.html')

    def test_game_view(self):
        url = self.client.get('/Game')
        self.assertEqual(url.status_code, 301)
        self.assertTemplateUsed('locationgameapp/Game.html')

    def test_add_admin_view(self):
        url = self.client.get('/AddAdmin')
        self.assertEqual(url.status_code, 301)
        self.assertTemplateUsed('locationgameapp/addAdmin.html')
    
    def test_add_location_view(self):
        url = self.client.get('/AddLocations')
        self.assertEqual(url.status_code, 301)
        self.assertTemplateUsed('locationgameapp/addLocations.html')

    def test_update_profile_view(self):
        url = self.client.get('/UpdateProfile')
        self.assertEqual(url.status_code, 301)
        self.assertTemplateUsed('locationgameapp/UpdateProfile.html')

    