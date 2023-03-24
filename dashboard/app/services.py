from django_grpc_framework import generics
from django.db.models import F
from .models import Product
from .utils import get_random_user
from .serializers import ProductProtoSerializer
# import user_pb2
# import product_pb2
from micorservice_demo_with_grpc_shared_utils import user_pb2, product_pb2

class ProductService(generics.ModelService):
    """
    gRPC services for products
    """
    queryset = Product.objects.all()
    serializer_class = ProductProtoSerializer
    look_up_field = 'id'

    def LikeProduct(self, request, context):
        product = self.get_object()
        # product.likes = F('likes') + 1 # This runs on db level and obj will have to refreshed to get update
        product.likes = product.likes + 1
        product.save()
        serialized = self.serializer_class(product).message
        return product_pb2.LikeProductResponse(product=serialized)


class UserService(generics.GenericService):

    def GetUser(self, request, context):
        user = get_random_user()
        return user_pb2.GetUserResponse(id=str(user.id))
