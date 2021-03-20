from django.shortcuts import render
from .models import Contact
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.urls import reverse_lazy
from django.db.models import Q

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

class SearchResultsView(generic.ListView):
    model = Contact
    template_name = 'pb/search_results.html'
#    queryset = Contact.objects.all()
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Contact.objects.filter(
            Q(fname__icontains = query) | Q(lname__icontains = query)

        )