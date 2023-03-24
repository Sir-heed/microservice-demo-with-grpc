# import product_receiver_pb2_grpc
from .services import ProductService
from micorservice_demo_with_grpc_shared_utils import product_receiver_pb2_grpc

def grpc_handlers(server):
    product_receiver_pb2_grpc.add_ProductReceiverServiceServicer_to_server(ProductService.as_servicer(), server)