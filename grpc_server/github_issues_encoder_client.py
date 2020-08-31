from __future__ import print_function
import logging

import grpc

import github_issues_encoder_pb2
import github_issues_encoder_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    issue = "AppDomain.SetPrincipalPolicy(PrincipalPolicy.WindowsPrincipal) works only once. Setting the PrincipalPolicy on the current AppDomain to WindowsPrincipal works only for the first thread being started. Any subsequent thread has Thread.CurrentPrincipal evaluated to NULL."
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = github_issues_encoder_pb2_grpc.EncoderStub(channel)
        response = stub.Encode(github_issues_encoder_pb2.Issue(text=issue))
    print("Greeter client received: ")
    print(f"Input_ids : {response.input_ids}")
    print(f"Attention_mask : {response.attention_mask}")


if __name__ == '__main__':
    logging.basicConfig()
    run()