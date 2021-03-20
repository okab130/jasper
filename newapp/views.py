from django.shortcuts import render
from django.views.generic import TemplateView

class SampleTemplateView(TemplateView):
    template_name = "newapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
#        context["foo"] = "bar"
        
        context["foo1"] = self.template_name
        context["foo2"] = "aa"
        context["foo3"] = "bb"
        context["foo4"] = "cc"
        context["foo5"] = "あああああああああああああああああああああああああああああああ"
        context["foo6"] = "あああああああああああああああああああああああああああああああ"
        context["foo7"] = "あああああああああああああああああああああああああああああああ"
        context["foo8"] = "あああああああああああああああああああああああああああああああ"
        context["foo9"] = "あああああああああああああああああああああああああああああああ"
        return context

