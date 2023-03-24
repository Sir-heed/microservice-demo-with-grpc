from django_grpc_framework import generics, mixins
from .models import Product
from .serializers import ProductReceiverProtoSerializer
# import product_receiver_pb2
from micorservice_demo_with_grpc_shared_utils import product_receiver_pb2

# class ProductService(generics.ModelService):
class ProductService(mixins.CreateModelMixin,
                    mixins.PartialUpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericService):
    """
    gRPC services for products
    """
    queryset = Product.objects.all()
    serializer_class = ProductReceiverProtoSerializer

    def get_object(self):
        "Using this because lookup field can only be access via request.product_receiver.product_id"
        request = self.request
        if hasattr(request, 'product_receiver'):
            product_id = request.product_receiver.product_id
        else:
            product_id = request.product_id
        return Product.objects.get(product_id=product_id)


    def CreateProductFromReceiver(self, request, context):
        product = self.Create(request.product_receiver, context)
        # serializer = product_receiver_pb2.ProductReceiver(product_id=str(product.product_id), title=product.title, image=product.image)
        serializer = self.serializer_class(product).message
        return product_receiver_pb2.CreateProductFromReceiverResponse(product_receiver=serializer)
    

    def Update(self, request, context):
        product = self.PartialUpdate(request.product_receiver, context)
        serializer = self.serializer_class(product).message
        return product_receiver_pb2.UpdateByIdResponse(product_receiver=serializer)
    

    def Delete(self, request, context):
        return self.Destroy(request, context)
    
    
