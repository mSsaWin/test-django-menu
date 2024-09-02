from django.contrib import admin
from django.urls import path, include

from menu import views

urlpatterns = [
    path('admin/dynamic_raw_id/', include('dynamic_raw_id.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<slug:menu_slug>/<slug:item_slug>/', views.menuitem_detail, name='menuitem_detail')
]