from django.contrib import  admin
from django.urls import path, include
#import textdata.textdata1.views as views
# import repairshop.shop.views as views
from django.conf import settings
from django.conf.urls.static import static
from shop import views

from rest_framework.routers import DefaultRouter
"""router = DefaultRouter()
router.register('text/',views.text_view,basename='text')"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('chooseUs/',views.chooseUs),
    path('ourServices/',views.ourServices),
    path('galleryImages/', views.galleryImages),
    path('Repairing/', views.getRepairing),
    path('contactUs/', views.contactUs),
    path('Accessories/', views.getAccessories)
    #path('', include(router.urls)),
    #path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
