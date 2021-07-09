from django.contrib import admin
from .models import Enquiry,GalleryImages,ShopDetails,ShopHistory,ClientReviews,ChooseUs,Staff,Service,Quote,LaptopRepairing,MobileRepairing,ContactUs,Carousal


# Register your models here.
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['receiptID', 'enquiryDate', 'customerName','contactNo','email','address','image','deviceType','brand','deviceModel','serialNo','problemCategory','problem',
                    'problemDescription','deviceCondition','estimatedCost','advance','status']


@admin.register(GalleryImages)
class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = ['imageID','order','title','description','images']


@admin.register(ShopDetails)
class ShopDetailsAdmin(admin.ModelAdmin):
    list_display = ['shopID','shopName','shopOwnerName','shop_address','shop_email','services','accountNO','mobileNO','shopLandlineNO','shopImage','working_time']

@admin.register(ShopHistory)
class ShopHistoryAdmin(admin.ModelAdmin):
    list_display = ['happy_customers','mobile_repairs','laptop_repairs','tablet_repairs','pc_repairs','yearsofexperience']

@admin.register(ClientReviews)
class ClientReviewsAdmin(admin.ModelAdmin):
    list_display = ['cliendID','clientreviewDate','clientName','clientdesignation','clientimage','textdetail']

@admin.register(ChooseUs)
class ChooseUsAdmin(admin.ModelAdmin):
    list_display = ['id','icon','title','textdetail']

@admin.register(Carousal)
class ChooseUsAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['StaffID','staffimage','StaffName','Staffdesignation','staffdetail']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['serviceID','image','title','detail']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quotId','firstname','lastname','email','phoneNO','description']

@admin.register(LaptopRepairing)
class LaptopRepairingAdmin(admin.ModelAdmin):
    list_display = ['imageID','images','order','title','description']

@admin.register(MobileRepairing)
class MobileRepairingAdmin(admin.ModelAdmin):
    list_display = ['imageID','images','order','title','description']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['contactId','fullName','email','subject','phoneNO','message']
# Register your models here.


