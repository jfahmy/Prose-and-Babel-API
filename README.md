# Prose-and-Babel-API: Experimenting with GRPC and prose generating scripts.

This respository holds the server code and resources needed to return Haikus, Markov Chain generated sentences, and Fibonacci poems, when they are requested from a GRPC client. My GRPC client repository [lives here](https://github.com/jfahmy/BabelBots). However, after downloading the ProseAndBabel_pb2.py and ProseAndBabel_pb2_grpc.py files, this server can be used with any client. When working with a GRPC API, these two files serve to define the rpc method calls that are available between the server and client. 

## Sample calls to the server in this repository: 

### Requesting a Haiku:

SAMPLE CALL - This will return a haiku as a string:
response = stub.GetFib(ProseAndBabel_pb2.BabelRequest())
repsone.prose

### Requesting a Markov Sentence:

SAMPLE CALL - This will return a Markov sentence as a string:

response = stub.UserMarkov(ProseAndBabel_pb2.BabelRequest(ask=text))
response.prose

### Requesting a Fibonacci Poem:

SAMPLE CALL - This will return a Fibonacci poem as a string:
response = stub.GetFib(ProseAndBabel_pb2.BabelRequest())
response.prose



## How I setup this GRPC application:

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
