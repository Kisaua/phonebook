from django.db import models
from django.urls import reverse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(contactUrl):
    validate = URLValidator()
    validate(contactUrl)
    

# Create your models here.
class Contact(models.Model):
    fname = models.CharField('fname', max_length=50, help_text='Enter Firts name')
    lname = models.CharField('lname', max_length=50, help_text='Enter Last name')
#    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    city = models.CharField('City', max_length=50,  blank = True,  help_text='Enter City')
    address = models.CharField('Address', max_length=150, blank = True, help_text='Enter address')
    phone = models.CharField('Phone', max_length=9, help_text='Phone number')
    contactUrl = models.CharField('URL', max_length=250, null = True, blank = True, help_text='Enter valid web adsress', validators=[validate_url,])
    image = models.ImageField(upload_to='pb/static/images', blank = True,)

    def __str__(self): 
        return '%s, %s' % (self.fname, self.lname)

    def get_absolute_url(self):
        return reverse('contact-detail', args = [str(self.id)])
    
    class Meta:
        ordering = ['fname']
        unique_together = ('fname', 'lname')


# class ContactInfo (models.Model):
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
#     city = models.CharField('City', max_length=50,  blank = True,  help_text='Enter City')
#     address = models.CharField('address', max_length=150, blank = True, help_text='Enter address')
#     phone = models.CharField('Phone', max_length=9, help_text='Phone number')
#     contactUrl = models.CharField('URL', max_length=250, null = True, blank = True, help_text='Enter valid web adsress')
#     image = models.ImageField(upload_to='images', blank = True,)
    
