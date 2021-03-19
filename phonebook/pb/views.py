from django.shortcuts import render
from .models import Contact
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    contact_list = Contact.objects.all()
#    template = loader.get_template('pb/index.html')
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'pb/index.html', context)

class ContactDetailView(generic.DetailView):
    model = Contact

class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['fname','lname','city','address', 'phone', 'contactUrl', 'image']

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('index')