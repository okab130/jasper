from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post

class SampleTemplateView(TemplateView):
    template_name = "newapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
#        context["foo"] = "bar"
        
        context["foo1"] = self.template_name
        queryset = Post.objects.get(author='岡部')

        print(context)
        for aa in Post.objects.all():
            print(aa.author)

        return context

class SampleView(ListView):
    template_name = 'newapp/list.html'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context