# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShopDetails,ChooseUs,Service,ShopHistory,GalleryImages,Quote,Repairing,ContactUs,Carousal,Accessories
from .serilizer import ShopDetailsSerializer,QuoteSerializer,ChooseUsSerializer,ServiceSerializer,ShopHistorySerializer,GalleryImagesSerializer,RepairingSerializer,ContactUsSerializer,CarousalSerializer,AccessoriesSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST


@csrf_exempt
@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        list = []
        dict={}
        shopdetailobj = ShopDetails.objects.all().filter(status=True).last()
        serializer = ShopDetailsSerializer(shopdetailobj)
        dict['shop_detail'] = serializer.data
        # list.append(dict)
        ChooseUsobj = ChooseUs.objects.all()
        print(ChooseUsobj)
        for obj in ChooseUsobj:
            serializer = ChooseUsSerializer(obj)
            list.append(serializer.data)
            dict['chooseus'] = list


        Serviceobj = Service.objects.all()
        print(Serviceobj)
        lis = []
        for obj in Serviceobj:
            seri = ServiceSerializer(obj)
            lis.append(seri.data)
            dict['services'] = lis

        shophisobj = ShopHistory.objects.all().last()
        ser = ShopHistorySerializer(shophisobj)
        dict['shophistory'] = ser.data

        Carousalobj = Carousal.objects.order_by('id')
        li = []
        for obj in Carousalobj:
            serializer = CarousalSerializer(obj)
            li.append(serializer.data)
            dict['Carousal'] = li
        return Response(dict)

    if (request.method == 'POST'):
        print('home')
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            quotequrey = Quote.objects.all().last()
            print("quote",quotequrey)
            quoteser = QuoteSerializer(quotequrey)
            print('quoteser',quoteser.data)
            return Response({'msg': quoteser.data})

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def chooseUs(request):
    print('hy')
    if request.method == 'GET':
        ChooseUsobj = ChooseUs.objects.order_by('id')
        list = []
        print(ChooseUsobj)
        for obj in ChooseUsobj:
            serializer = ChooseUsSerializer(obj)
            list.append(serializer.data)

        return Response(list)



@api_view(['GET'])
def getAccessories(request):
    if request.method == 'GET':
        print('hy')
        Accobj = Accessories.objects.all()
        list = []
        print(Accobj)
        for obj in Accobj:
            serializer = AccessoriesSerializer(obj)
            list.append(serializer.data)

        return Response(list)

@api_view(['GET'])
def ourServices(request):
    service = []
    if request.method == 'GET':
        Serviceobj = Service.objects.all()
        for obj in Serviceobj:
            seri = ServiceSerializer(obj)
            service.append(seri.data)
        return Response(service)


@api_view(['GET'])
def galleryImages(request):
    print('images')
    galleryimg = []
    if request.method == 'GET':
        imgobj = GalleryImages.objects.all()
        for obj in imgobj:
            seri = GalleryImagesSerializer(obj)
            galleryimg.append(seri.data)
        return Response(galleryimg)



@api_view(['GET'])
def getRepairing(request):
    print('images')
    galleryimg = []
    if request.method == 'GET':
        imgobj = Repairing.objects.all()
        for obj in imgobj:
            seri = RepairingSerializer(obj)
            galleryimg.append(seri.data)
        return Response(galleryimg)



@api_view(['POST'])
def contactUs(request):
    if (request.method == 'POST'):
        print('home')
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            contactUsqurey = ContactUs.objects.all().last()
            # print("quote", contactUsqurey)
            contactusser = ContactUsSerializer(contactUsqurey)
            # print('quoteser', contactusser.data)
            return Response({'msg': contactusser.data})

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
