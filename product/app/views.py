import grpc
from django.db.utils import IntegrityError
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
# import requests
from .models import Product, ProductUser
# from .producer import publish
from .serializers import ProductSerializer
from django.conf import settings
# import user_pb2_grpc
# import user_pb2
# import product_pb2
# import product_pb2_grpc
from micorservice_demo_with_grpc_shared_utils import user_pb2_grpc, user_pb2, product_pb2, product_pb2_grpc

DASHBOARD_GRPC_SERVER = settings.DASHBOARD_GRPC_SERVER

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class LikeView(APIView):
    def get(self, _, pk):
        # req = requests.get('http://127.0.0.1:8000/api/user')
        # response = req.json()
        with grpc.insecure_channel(DASHBOARD_GRPC_SERVER) as channel:
            stub = user_pb2_grpc.UserServiceStub(channel)
            response = stub.GetUser(user_pb2.GetUserRequest())
            print(response, end='')
        try:
            product = Product.objects.get(pk=pk)
            product_user = ProductUser.objects.create(user_id=response.id, product_id=pk)
            # publish('product_liked', product.product_id)
            with grpc.insecure_channel(DASHBOARD_GRPC_SERVER) as channel:
                stub = product_pb2_grpc.ProductServiceStub(channel)
                response = stub.LikeProduct(product_pb2.LikeProductRequest(id=str(product.product_id)))
                print(response, end='')
            return Response({
                'messsage': 'Success'
            })
        except IntegrityError:
            return Response({
                'message': 'You already liked this product'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(req.json())