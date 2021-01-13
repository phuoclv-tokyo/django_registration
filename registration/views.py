from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "registration/index.html"



class ProductView(TemplateView):
    template_name = "product/product.html"
    

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm
from .forms import activate_user



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        #　認証トークンを検証して、
        result = activate_user(uidb64, token)
        # コンテストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result = result, **kwargs)
