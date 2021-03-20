from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)$', views.ContactDetailView.as_view(), name='contact-detail'),
    url(r'^create/$', views.ContactCreate.as_view(), name='contact_create'),
    url(r'^(?P<pk>\d+)/update/$', views.ContactUpdate.as_view(), name='contact_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ContactDelete.as_view(), name='contact_delete'),
    url(r'^search$', views.SearchResultsView.as_view(), name='search_results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)