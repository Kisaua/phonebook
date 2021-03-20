from django.test import TestCase

#from phonebook.phonebook.pb.models  import Contact
from pb.models  import Contact
from django.urls import reverse
# Create your tests here.

class ContactDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Contact.objects.create(
            fname= 'Vasiliy',
            lname='Pupkin',
            city = 'San Jose',
            address = 'apple alley 5',
            phone = '059654938',
            contactUrl = 'https://python.org',
            image = 'pb/static/images/IMG_0023.jpg'
            )
    
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/pb/1')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contact-detail', args = ['1',]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'pb/contact_detail.html')
