from django.urls import path
from .views import contact_view
from .views import about


urlpatterns = [
    path('', contact_view, name='contact'),  # Remove 'contact/'
    path('about/', about, name='about'),
]
