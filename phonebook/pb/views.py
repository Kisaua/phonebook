from django.shortcuts import render
from .models import Contact, ContactInfo
from django.views import generic

# Create your views here.
def index(request):
    contact_list = Contact.objects.all()
#    template = loader.get_template('pb/index.html')
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'pb/index.html', context)

class ContactInfoDetailView(generic.DetailView):
    model = Contact