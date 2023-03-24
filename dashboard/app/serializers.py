from .models import Product
from rest_framework import serializers
from django_grpc_framework import proto_serializers
# import product_pb2
from micorservice_demo_with_grpc_shared_utils import product_pb2


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = product_pb2.Product
        fields = ['id', 'title', 'image', 'likes']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'