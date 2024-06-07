from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home')
    path('admin/', admin.site.urls),
     path('home/', include('home.urls'))
]
