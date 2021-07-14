from django.conf.urls.static import static
from django.contrib import  admin
from django.urls import path
#import textdata.textdata1.views as views
# import repairshop.shop.views as views
from django.conf import settings
from shop import views

"""router = DefaultRouter()
router.register('text/',views.text_view,basename='text')"""


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/home/', views.home),
    path('api/chooseUs/',views.chooseUs),
    path('api/ourServices/',views.ourServices),
    path('api/galleryImages/', views.galleryImages),
    path('api/laptopRepairing/', views.laptopRepairing),
    path('api/mobileRepairing/', views.mobileRepairing),
    path('api/contactUs/', views.contactUs),
    path('api/carousal/', views.carousal)
    #path('', include(router.urls)),
    #path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
