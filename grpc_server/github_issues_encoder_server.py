from concurrent import futures
import logging
from transformers import RobertaTokenizerFast

import grpc

import github_issues_encoder_pb2
import github_issues_encoder_pb2_grpc

class Encoder(github_issues_encoder_pb2_grpc.EncoderServicer):

    def __init__(self, tokenizer, max_len) -> None:
        self.tokenizer = tokenizer
        self.max_len = max_len

    def Encode(self, request, context):
        encoded = self.tokenizer(request.text, padding='max_length', truncation=True, max_length=self.MAX_LEN)
        return github_issues_encoder_pb2.EncodedIssue(input_ids= encoded["input_ids"], attention_mask=encoded["attention_mask"])


def serve(tokenizer, max_len):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    github_issues_encoder_pb2_grpc.add_EncoderServicer_to_server(Encoder(tokenizer, max_len), server)
    server.add_insecure_port('[::]:50051')
    #server.add_secure_port('[::]:5001', )
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    tokenizer = RobertaTokenizerFast.from_pretrained("roberta-base")
    max_len = 128
    serve(tokenizer, max_len)