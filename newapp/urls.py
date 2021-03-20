from django.urls import path
from newapp.views import SampleTemplateView

urlpatterns = [
    path('sample', SampleTemplateView.as_view()),
]