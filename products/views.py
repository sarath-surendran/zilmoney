from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Products, Purchase
from .serializers import Itemviewserializer
# Create your views here.

# def home(request):
#     return render(request, 'home.html')

# def ItemDetails(request, item_id):
#     if request.method == 'GET':
#         try:
#             item = Products.objects.get(id=item_id)
#         except:
#             pass

class ItemDetail(APIView):
    def get(self, request, item_id):
        apply_discount = request.query_params.get('apply_discount')
        if apply_discount:
            try:
                item = Products.objects.get(id = item_id)
                serializer = Itemviewserializer(item)
                discount_percentage = 10
                data = serializer.data
                data['amount'] = (data['amount']*discount_percentage)/100
                return Response(data, status=status.HTTP_200_OK) 
                # return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'message':'Item doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                item = Products.objects.get(id = item_id)
                serializer = Itemviewserializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'message':'Item doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)


class PurchaseItem(APIView):
    def post(self, request):
        item_id = request.data["item_id"]
        quantity = request.data['quantity']
        
        try:
            item = Products.objects.get(id = item_id)
            if quantity > item.availiable_quantity:
                quantity = item.availiable_quantity
                item.availiable_quantity = 0
                item.save()
            else:
                item.availiable_quantity -= quantity
                item.save()
            Purchase.objects.create(
                product = item,
                purchased_quantity = quantity,
                total_amount = quantity * item.amount
            )
            return Response({'message':"Purchase Successfull"}, status=status.HTTP_200_OK)
            
        except:
            return Response({'message':'Item doesnot exist'}, status=status.HTTP_400_BAD_REQUEST)
        

        
