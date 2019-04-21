# Prose-and-Babel-API: 
## Experimenting with GRPC and prose generating scripts

This respository holds the server code and resources needed to return Haikus, Markov Chain generated sentences, and Fibonacci poems, when they are requested by a GRPC client. My GRPC client repository [lives here](https://github.com/jfahmy/BabelBots). ProseAndBabel_pb2.py and ProseAndBabel_pb2_grpc.py in this repository define the rpc method calls that are available to clients. 

## My Bots

The end result of this project was a few friendly Twitter bots putting content out into the world:
[@WorldFameBot](https://twitter.com/WorldFameBot)
[@BardFibonacci](https://twitter.com/BardFibonacci)
[@BotQuixotic](https://twitter.com/BotQuixotic)

Tweet at them and they will tweet back with content scraped from your own Twitter feed!

## Project Diagram
![Project Diagram](https://github.com/jfahmy/Images/blob/master/Babel%20Bots%20Diagram%20(1).png)

## Sample calls to the server in this repository: 

### Requesting a Haiku:

This call will return a haiku as a string:

response = stub.GetFib(ProseAndBabel_pb2.BabelRequest())

response.prose

### Requesting a Markov Sentence:

This call will return a Markov sentence as a string:

response = stub.UserMarkov(ProseAndBabel_pb2.BabelRequest(ask=text))

response.prose

### Requesting a Fibonacci Poem:

This call will return a Fibonacci poem as a string:

response = stub.GetFib(ProseAndBabel_pb2.BabelRequest())

response.prose



## Steps for setting up a GRPC application:

1. DEFINE THE SERVICE
    - specify a named service in your .proto file then define the rpc methods inside it (remote procedural calls)
    - Also define protocol buffer message type definitions for the request and response types to be used in our service methods - formal definition of how your api works - inputs and outputs.
2. GENERATE CLIENT AND SERVER CODE
    - pip install grpcio-tools (though it may be already installed of course)
    - python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/ProseAndBabel.proto
    - Running the above command from your project directory will create or regenerate the pb2.py and pb2_grpc.py code. This is running the compiler.
    - File directories in the above command will vary depending on where you are in your file structure. 
3. CREATE THE SERVER
    - Implement the servicer interface generated from our service definition with functions that perform the actual “work” of the service. File should be called [name of service]_server.py
    - Run the thing!
4. CREATE THE CLIENT
    - Create a stub - We instantiate the [NameOfApp]Stub class of the pb2_grpc module, generated from our .proto
    - Call your service methods 
