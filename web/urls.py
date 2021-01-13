from django.contrib import admin
from django.urls import path
from website.views import index, login, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beranda/', index),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup')
]
