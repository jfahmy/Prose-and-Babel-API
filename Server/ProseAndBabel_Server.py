from concurrent import futures
import time
import haiku
import markovOrder1
import scrape
import readmarkov

import grpc

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class ProseAndBabel(ProseAndBabel_pb2_grpc.ProseAndBabelServicer):


    def GetHaiku(self, request, context):
        # try and except makes sure the call functions whether or not URL is provided by client
        try:
            request.ask
            full_text = scrape.full_text(request.ask)
            prose = haiku.build_haiku(full_text)
            return ProseAndBabel_pb2.Babel(prose=prose)
        except:
            full_text = scrape.full_text("http://www.gutenberg.org/cache/epub/996/pg996.html")
            prose = haiku.build_haiku(full_text)
            return ProseAndBabel_pb2.Babel(prose=prose)

    def GetBabel(self, request, context):
        full_text = scrape.full_text(request.ask)
        return ProseAndBabel_pb2.Babel(prose=markov.get_sentence(full_text))

    def UserMarkov(self, request_iterator, context):
        return ProseAndBabel_pb2.Babel(prose=markovOrder1.generate_sentence(request_iterator.tweets)+ " #BabelFrom")

    def UserHaiku(self, request, context):
        return ProseAndBabel_pb2.Babel(prose=haiku.build_haiku(request.tweets) + " #HaikuFrom")

    # Not working
    # def GetCelebMarkov(self, request, context):
    #     response = readmarkov.generate_sentence(chain)
    #     return ProseAndBabel_pb2.CelebBabel(tweet=response[0], source=response[1])


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
