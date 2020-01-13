import greeter_pb2_grpc
import greeter_pb2
import grpc
from concurrent import futures
import logging

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message="Hello %s" % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info(msg="listening on port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()