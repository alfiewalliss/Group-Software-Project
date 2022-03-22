from django.test import SimpleTestCase

# Tests that each page is located at the expected URL and returns the expected status code
class TestUrls(SimpleTestCase):

    def test_game_url(self):
        url = self.client.get('/Game')
        self.assertEqual(url.status_code, 301)

    def test_add_locations_url(self):
        url = self.client.get('/AddLocations')
        self.assertEqual(url.status_code, 301)

    def test_add_admin_url(self):
        url = self.client.get('/AddAdmin')
        self.assertEqual(url.status_code, 301)
    
    def test_login_url(self):
        url = self.client.get('/login')
        self.assertEqual(url.status_code, 301)

    def test_sign_up_url(self):
        url = self.client.get('/signUp')
        self.assertEqual(url.status_code, 301)

    def test_logout_url(self):
        url = self.client.get('/logout')
        self.assertEqual(url.status_code, 301)

    def test_password_reset_url(self):
        url = self.client.get('/password-reset')
        self.assertEqual(url.status_code, 301)

    def test_password_reset_done_url(self):
        url = self.client.get('/password-reset/done')
        self.assertEqual(url.status_code, 301)

    def test_password_reset_confirm_url(self):
        url = self.client.get('/password-reset-confirmMTY/set-password')
        self.assertEqual(url.status_code, 301)

    def test_password_reset_complete_url(self):
        url = self.client.get('/password-reset-complete')
        self.assertEqual(url.status_code, 301)
