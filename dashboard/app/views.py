# from product.producer import publish
import grpc
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from .utils import get_random_user
from .serializers import ProductSerializer
from .models import Product, User
# import product_receiver_pb2
# import product_receiver_pb2_grpc
from micorservice_demo_with_grpc_shared_utils import product_receiver_pb2, product_receiver_pb2_grpc

PRODUCT_GRPC_SERVER = settings.PRODUCT_GRPC_SERVER

class ProductViewSet(viewsets.ModelViewSet):#
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        # publish('product_created', serializer.data)
        with grpc.insecure_channel(PRODUCT_GRPC_SERVER) as channel:
            stub = product_receiver_pb2_grpc.ProductReceiverServiceStub(channel)
            product_ser = product_receiver_pb2.ProductReceiver(product_id=str(product.id), title=product.title, image=product.image)
            res = stub.CreateProductFromReceiver(product_receiver_pb2.CreateProductFromReceiverRequest(product_receiver=product_ser))
            print(res, end='')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        product = self.get_object()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):
        product = self.get_object()
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # publish('product_updated', serializer.data)
        with grpc.insecure_channel(PRODUCT_GRPC_SERVER) as channel:
            stub = product_receiver_pb2_grpc.ProductReceiverServiceStub(channel)
            product_data = {
                'product_id' : str(product.id),
                'title': product.title,
                'image': product.image
            }
            product_ser = product_receiver_pb2.ProductReceiver(**product_data)
            res = stub.Update(product_receiver_pb2.UpdateByIdRequest(product_receiver=product_ser))
            print(res, end='')
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk):
        product = self.get_object()
        # publish('product_deleted', pk)
        with grpc.insecure_channel(PRODUCT_GRPC_SERVER) as channel:
            stub = product_receiver_pb2_grpc.ProductReceiverServiceStub(channel)
            res = stub.Delete(product_receiver_pb2.DeleteByIdRequest(product_id=str(product.id)))
            print(res, end='')
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        user = get_random_user()
        return Response({
            'id': user.id
        }, status=status.HTTP_200_OK)
    
    def post(self, _):
        User.objects.create()
        return Response(status=status.HTTP_201_CREATED)