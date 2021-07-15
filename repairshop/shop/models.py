from django.db import models

# Create your models here.
class Enquiry(models.Model):
	PROBLEM_CATEGORY_CHOICES = (
		('LP','Laptop'),
		('MO','Mobile'),
		('TB', 'Tablet'),
		('PC', 'PcComputer'),
		('SF', 'Softwear'),
		('OT', 'Others'),
	)

	STATUS_CHOICES = (
		('EN','Enquired'),
		('CH','Checked'),		# This is amazing
		('RE','Repaired'),		# Changed from Update Form when Components are added and Repair Charge is added
		('CO','Completed'),		# Changed to when Final Receipt is Generated
		('RJ','Rejected'),
	)

	receiptID = models.AutoField(primary_key=True)
	enquiryDate = models.DateField()

	customerName = models.CharField(max_length = 50)
	contactNo = models.CharField(max_length = 20)
	email = models.CharField(max_length = 50, blank=True)
	address = models.TextField(blank=True)
	image = models.ImageField(upload_to='shop/images', default='')

	deviceType = models.CharField(max_length = 50)
	brand = models.CharField(max_length = 50, blank=True)
	deviceModel = models.CharField(max_length = 50)
	serialNo = models.CharField(max_length = 50, blank=True)

	problemCategory = models.CharField(max_length = 3, choices = PROBLEM_CATEGORY_CHOICES)
	problem = models.CharField(max_length = 50)
	problemDescription = models.TextField(blank=True)

	deviceCondition = models.TextField(blank=True)

	estimatedCost = models.IntegerField()
	advance = models.IntegerField(default=0)

	status = models.CharField(max_length=3, choices = STATUS_CHOICES, default='EN')

	def __str__(self):
		return str(self.receiptID) + " : "  + self.status + " : "  + self.customerName + " : " + self.brand + " " + self.deviceModel

class TestDetail(models.Model):
	Enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
	actualProblem = models.CharField(max_length = 50)
	actualProblemDescription = models.TextField(blank=True)

	def __str__(self):
		return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + self.Enquiry.customerName + " : " + self.actualProblem

class ShopDetails(models.Model):
	SERVICES = (
		('LP', 'Laptop repairing'),
		('MO', 'Mobile repairing'),
		('TB', 'Tablet repairing'),
		('PC', 'PcComputer repairing'),
		('SF', 'Softwear repairing'),
		('OT', 'Others'),
	)
	shopID = models.AutoField(primary_key=True)
	shopName = models.CharField(max_length = 50)
	shopOwnerName = models.CharField(max_length = 50)
	shop_address = models.CharField(max_length = 200)
	shop_email = models.CharField(max_length = 50)
	services = models.CharField(max_length = 10, choices = SERVICES)
	accountNO = models.CharField(max_length = 100)
	mobileNO = models.CharField(max_length=100)
	shopLandlineNO = models.CharField(max_length=100)
	shopImage = models.ImageField(upload_to='shop/images', default='')
	working_time = models.CharField(max_length=50)
	isdeleted = models.BooleanField(default=False, null=True)
	status = models.BooleanField(default=False, null=True)
	# def __str__(self):
	# 	return str(self.shopID) + " : " + str(self.shopName) + " : " + str (self.shopOwnerName)



class GalleryImages(models.Model):
	imageID = models.AutoField(primary_key=True)
	order = models.CharField(max_length=100)
	title = models.CharField(max_length=250)
	description = models.TextField()
	images = models.ImageField(upload_to='shop/images', default='')

	def __str__(self):
		return self.title

class Repairing(models.Model):
	imageID = models.AutoField(primary_key=True)
	images = models.ImageField(upload_to='shop/images', default='')
	order = models.CharField(max_length=100)
	title = models.CharField(max_length=250)
	description = models.TextField()



	def __str__(self):
		return self.title

class ShopHistory(models.Model):
	shopdetails = models.OneToOneField(ShopDetails, on_delete=models.CASCADE, primary_key=True)
	happy_customers = models.CharField(max_length=100)
	mobile_repairs = models.CharField(max_length=250)
	laptop_repairs = models.CharField(max_length=250)
	tablet_repairs = models.CharField(max_length=250)
	pc_repairs = models.CharField(max_length=250)
	yearsofexperience = models.CharField(max_length=250)

class ClientReviews(models.Model):
	cliendID = models.AutoField(primary_key=True)
	clientreviewDate = models.DateField()
	clientName = models.CharField(max_length = 50)
	clientdesignation = models.CharField(max_length=50)
	clientimage = models.ImageField(upload_to='shop/images', default='')
	textdetail = models.TextField(blank=True)

class ChooseUs(models.Model):
	icon = models.CharField(default='', max_length=100)
	title = models.CharField(max_length = 50)
	textdetail = models.TextField(blank=True)

class Carousal(models.Model):
	image = models.ImageField(upload_to='shop/images',default='')
	title = models.CharField(max_length = 50)
	description = models.TextField(blank=True)

class Accessories(models.Model):
	image = models.ImageField(upload_to='shop/images',default='')
	title = models.CharField(max_length = 50)
	description = models.TextField(blank=True)


class Staff(models.Model):
	StaffID = models.AutoField(primary_key=True)
	staffimage = models.ImageField(upload_to='shop/images', default='')
	StaffName = models.CharField(max_length = 50)
	Staffdesignation = models.CharField(max_length=50)
	staffdetail = models.TextField(blank=True)

class Service(models.Model):
	serviceID = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to='shop/images', default='')
	title= models.CharField(max_length = 50)
	detail = models.TextField(blank=True)
	type = models.CharField(max_length=50)



class Quote(models.Model):
	quotId= models.AutoField(primary_key=True)
	firstname= models.CharField(max_length = 50)
	lastname = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	phoneNO = models.CharField(max_length=50)
	description = models.TextField(blank=True)


class ContactUs(models.Model):
	contactId = models.AutoField(primary_key=True)
	fullName = models.CharField(max_length=100)
	email = models.CharField(max_length=100, unique=True)
	subject = models.CharField(max_length=100)
	phoneNO = models.CharField(max_length=50)
	message = models.TextField(blank=True)

