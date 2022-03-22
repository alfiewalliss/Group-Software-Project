from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail

User = get_user_model()

class TestForms(TestCase):

    # Sets up a new user
    def setUp(self):
        newUser = User(email='test@test.com', username='test_user', first_name='Tess', last_name='Ting')
        newUser_password = 'ThisIsATestPassword99'
        self.newUser_password = newUser_password
        newUser.set_password(newUser_password)
        newUser.save()
        self.newUser = newUser


    # Tests that the user is created
    def test_user_is_created(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)


    # Tests that the user password is created and correct
    def test_user_password_is_created(self):
        newUser = User.objects.get(username="test_user")
        self.assertTrue(newUser.check_password(self.newUser_password))

    
    # Tests that the user password can't be a false value
    def test_user_password_not_false(self):
        newUser = User.objects.get(username="test_user")
        self.assertFalse(newUser.check_password("False Password"))


    # Tests that the email to reset password is sent
    def test_email_sent(self):
        mail.send_mail('subject', 'message', 'the.snail.game123@gmail.com', ['test@test.com'], fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
    

    # Tests that the contents of the email is corrent
    def test_mail_contents(self):
        mail.send_mail('subject', 'message', 'the.snail.game123@gmail.com', ['test@test.com'], fail_silently=False)
        self.assertEqual(mail.outbox[0].body, 'message')
        self.assertEqual(mail.outbox[0].subject, 'subject')


    ## Tests that all labels are correct
    def test_first_name_label(self):
        name = User.objects.get(id=1)
        label = name._meta.get_field('first_name').verbose_name
        self.assertEqual(label, 'first name')

    def test_last_name_label(self):
        name = User.objects.get(id=1)
        label = name._meta.get_field('last_name').verbose_name
        self.assertEqual(label, 'last name')

    def test_email_label(self):
        email = User.objects.get(id=1)
        label = email._meta.get_field('email').verbose_name
        self.assertEqual(label, 'email address')

    def test_username_label(self):
        username = User.objects.get(id=1)
        label = username._meta.get_field('username').verbose_name
        self.assertEqual(label, 'username')

    def test_password_label(self):
        password = User.objects.get(id=1)
        label = password._meta.get_field('password').verbose_name
        self.assertEqual(label, 'password')
