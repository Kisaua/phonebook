from django.shortcuts import render
from .models import Contact
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.forms import ModelForm, TextInput, ImageField

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

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'fname': TextInput(attrs={'placeholder': Contact._meta.get_field('fname').help_text, 'class' : 'form-control mt-2',}),
            'lname': TextInput(attrs={'placeholder': Contact._meta.get_field('lname').help_text  , 'class' : 'form-control mt-2',}),
            'city': TextInput(attrs={'placeholder': Contact._meta.get_field('city').help_text  , 'class' : 'form-control mt-2',}),
            'address': TextInput(attrs={'placeholder': Contact._meta.get_field('address').help_text  , 'class' : 'form-control mt-2',}),
            'phone': TextInput(attrs={'placeholder': Contact._meta.get_field('phone').help_text  , 'class' : 'form-control mt-2',}),
            'contactUrl': TextInput(attrs={'placeholder': Contact._meta.get_field('contactUrl').help_text  , 'class' : 'form-control mt-2',})
        
        }

class ContactCreate(CreateView):
    model = Contact
#    fields = '__all__'
    form_class = ContactForm

class ContactUpdate(UpdateView):
    model = Contact
#    fields = ['fname','lname','city','address', 'phone', 'contactUrl', 'image']
    form_class = ContactForm

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
