from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.index, name='index'),
     path('doctor/',include('doctor.urls')),
     path('patient/',include('patient.urls')),
     path('service/',include('service.urls')),
     path('contact/',include('contact.urls')),
     path('appointment/',include('appointment.urls')),
     path('accounts/',include('accounts.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)