# import product_pb2_grpc
# import user_pb2_grpc
from .services import ProductService, UserService
from micorservice_demo_with_grpc_shared_utils import product_pb2_grpc, user_pb2_grpc

def grpc_handlers(server):
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService.as_servicer(), server)
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService.as_servicer(), server)