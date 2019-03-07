from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about-us/', aboutUsView, name='about-us')
]