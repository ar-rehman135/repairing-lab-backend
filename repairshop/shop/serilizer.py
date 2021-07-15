from rest_framework import serializers
from .models import ShopDetails,Quote,ChooseUs,Service,ShopHistory,GalleryImages,Repairing,ContactUs,Carousal,Accessories

class ShopDetailsSerializer(serializers.ModelSerializer):


    class Meta:
        model = ShopDetails
        fields = "__all__"

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"

class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class ShopHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopHistory
        fields = "__all__"

class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = "__all__"

class RepairingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repairing
        fields = "__all__"



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"

class CarousalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousal
        fields = "__all__"

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = "__all__"
    # def validate(self, data):  # data come from python dictionary
    #     text = data.get("text")  # get the get field attribute in dict
    #     print(text)
    #     return data