import greeter_pb2_grpc
import greeter_pb2
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = greeter_pb2_grpc.GreeterStub(channel)
request = greeter_pb2.HelloRequest(name="Github")
response = stub.SayHello(request)
print(response.message)