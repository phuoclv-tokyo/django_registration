from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name="index"),
    path('product/', login_required(views.ProductView.as_view()), name="product"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name="activate"),
]

