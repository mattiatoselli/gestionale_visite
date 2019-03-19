"""gestionale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from pianificazione_visite import views
#Add URL maps to redirect the base URL to our application
admin.site.site_header = settings.ADMIN_SITE_HEADER #import the change in the admin site header
admin.site.site_title = "Amministrazione sessioni di visita"
admin.site.index_title = "BENVENUTO IN HCT SOLUTIONS"
urlpatterns = [
	path('admin/', admin.site.urls),
	path('pianificazione_visite/', include('pianificazione_visite.urls')),
	path('', admin.site.urls), #controllare 05-05-2019
	]
# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)