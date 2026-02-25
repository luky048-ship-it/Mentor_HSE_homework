import grpc
import calculator_pb2 as pb2
import calculator_pb2_grpc as pb2_grpc


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.CalculatorStub(channel)

        r1 = stub.Add(pb2.AddRequest(a=2, b=3))
        print("Add(2,3) =", r1.result)

        r2 = stub.Hello(pb2.HelloRequest(name="Valera"))
        print("Hello =", r2.greeting)


if __name__ == "__main__":
    main()

