from django.urls import path
from .views import News,Home,Contact

urlpatterns = [
    path('News/', News, name='News'),
    path('', Home, name='Home'),
    path('Contact/', Contact, name='Contact'),
]
