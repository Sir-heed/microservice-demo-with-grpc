from rest_framework import serializers
from django_grpc_framework import proto_serializers
from .models import Product
# import product_receiver_pb2
from micorservice_demo_with_grpc_shared_utils import product_receiver_pb2


class ProductReceiverProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = product_receiver_pb2.ProductReceiver
        fields = ['product_id', 'title', 'image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'