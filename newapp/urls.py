from django.urls import path
from newapp.views import SampleTemplateView,SampleView

urlpatterns = [
    path('sample', SampleTemplateView.as_view()),
    path('list',SampleView.as_view()),
]