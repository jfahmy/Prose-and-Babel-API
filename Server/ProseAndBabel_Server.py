from concurrent import futures
import time
import haiku
import markov

import grpc

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class ProseAndBabel(ProseAndBabel_pb2_grpc.ProseAndBabelServicer):

    def GetHaiku(self, request, context):
        return ProseAndBabel_pb2.Babel(response=haiku.build_haiku(request.ask))

    def GetBabel(self, request,context):
        return ProseAndBabel_pb2.Babel(response=markov.get_sentence(request.ask))

def serve():
 server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
 ProseAndBabel_pb2_grpc.add_ProseAndBabelServicer_to_server(ProseAndBabel(), server)
 server.add_insecure_port('[::]:50050')
 server.start()
 try:
   while True:
     time.sleep(_ONE_DAY_IN_SECONDS)
 except KeyboardInterrupt:
   server.stop(0)

if __name__ == '__main__':
 serve()
