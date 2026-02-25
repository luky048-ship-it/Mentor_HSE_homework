from concurrent import futures
import grpc

import calculator_pb2 as pb2
import calculator_pb2_grpc as pb2_grpc


class CalculatorService(pb2_grpc.CalculatorServicer):
    def Add(self, request: pb2.AddRequest, context: grpc.ServicerContext) -> pb2.AddResponse:
        return pb2.AddResponse(result=request.a + request.b)

    def Hello(self, request: pb2.HelloRequest, context: grpc.ServicerContext) -> pb2.HelloResponse:
        name = (request.name or "").strip() or "world"
        return pb2.HelloResponse(greeting=f"Hello, {name}!")


def serve(host: str = "0.0.0.0", port: int = 50051) -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"gRPC server listening on {host}:{port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

