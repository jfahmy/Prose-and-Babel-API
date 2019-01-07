# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
# WORKDIR /app
ADD Server /

# Copy the current directory contents into the container at /app
# COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install time
# RUN pip install concurrent
RUN pip install grpc
RUN pip install grpcio-tools
# RUN pip install scrape
RUN pip install nltk
RUN pip install cmudict
RUN python -m nltk.downloader cmudict
# RUN pip install nltk.corpus
# RUN pip install random
# RUN pip install re
RUN pip install bs4
RUN pip install requests
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port available to the world outside this container?
EXPOSE 50050

# Define environment variable
# ENV NAME World

# Run this when the container launches
CMD ["python", "ProseAndBabel_Server.py"]
