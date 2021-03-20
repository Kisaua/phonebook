from django.test import TestCase

#from phonebook.phonebook.pb.models  import Contact
from pb.models  import Contact
# Create your tests here.
class ContactModelTest(TestCase):
    
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
    def test_fname_label(self):
        contact=Contact.objects.get(id=1)
        field_label = contact._meta.get_field('fname').verbose_name
        self.assertEquals(field_label,'First name')

    def test_get_absolute_url(self):
        contact=Contact.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(contact.get_absolute_url(), '/pb/1')