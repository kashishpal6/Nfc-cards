"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('auth_app.urls')),
    path('contact/',include('contact_page.urls')),
    path('products/',include('products.urls')),
    path('variant/',include('variant.urls')),
    path('services/',include('services.urls')),
    path('cart/',include('AddToCart.urls')),
    path('purchase/',include('purchase.urls')),
    path('payment/',include('payment.urls')),
    path('query_ticket/',include('query_ticket.urls')),
    path('return_page/',include('return_page.urls')),
    path('banner/',include('banner.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "NFC Cards Admin"
admin.site.site_title = "NFC Cards Admin Portal"
admin.site.index_title = "Welcome to NFC Cards Portal"


