# API Requests

Now that we have a basic data model implemented and organized, let's focus on acquiring data for our music store. To accomplish this, we will look at how to call RESTful APIs using the requests module. 

**Note**: There are a lot of details that go into understanding amd working with APIs and we will only be scratching the surface here.

## What is an API? 

API stands for Application Programming Interface and the most general definition pretty much follows this acronym; an API is a *interface* between a client and server that aids in *programming* client *applications*. If you are utilizing an API developed by some other party, then your application is the client and the host of the API is the server. 

One form of an API that you are already using is the Python standard library. In this case, the server and client are on the same machine. An example of an API that you will utilize later in DU (either directly or indirectly) is the Java Database Connection API (JDBC). This API can be used to communicate with most databases regardless of the language or tool you are using to call.

## Web Based REST APIs

For this module, we'll focus on Web based APIs. These APIs are generally used to retrieve or modify data and are the backbone of most web based applications. They are many different standards of Web based APIs including SOAP, REST, and GraphQL; each standard puts constraints on how the interface can be defined and what the expectations are for the client and or service. For now, we'll focus on REST.

There are several architectural standards that should be adhered to in a REST API; however, listing all of them would be too much to focus on here. So instead we will focus on three of the most foundational aspects:
1. An endpoint or base url
2. Use of standard HTTP methods (GET, POST, etc.)
3. Statelessness - client context is not stored on the server

In the exercises that follow each of these three aspects will become more apparent.

### Exercise 1

Go to the [Last.FM API](https://www.last.fm/api/) documentation page and find one endpoint that uses a GET method and one endpoint that uses a POST method.

### Exercise 2

Sign up for an application account [here](https://www.last.fm/api/account/create), save your credentials, then examine the documentation further to discover how *client context* is passed in each request to the server.

## Python's *Requests* Module

Most high level programming languages have methods devoted to making api requests in their standard library; however, there is also almost always a third party library that makes common methods even easier. In this learning module we are going to work with such a library: `requests`

Using the `requests` library is very simple. First make sure to install it using pip:

```bash
pip3 install requests
```

Then, invoking a GET request is as simple as passing the url and parameters as a dictionary.

```python
import os 
from requests import get

url = "http://ws.audioscrobbler.com/2.0/"
params = {
    "method": "chart.gettopartists",
    "api_key": os.environ.get("API_KEY"), # avoid hard coding secrets
    "format": "json",
    "limit": 10
}
response = get(url, params)

data = response.json()
print(data)
```

Typically, the response from an API is some standard format such as JSON or XML. In this case, the requested result format is JSON which we can very quickly turn into a dictionary using the `.json()` method call on the response. We will look into JSON more in the next module.

Other HTTP methods like POST have similar function implementations on the `requests` module, but we will limit ourselves to GET for now.

### Exercise 3

Use your own API KEY to get a list of the top 100 artist names in the USA (hint: the ISO standard country name is "United States").

### Exercise 4

Finish the methods stubbed out in the new `generate.py` file by calling the appropriate APIs and transforming the results. When you're done, run the file to generate your own store JSON file for use in the next module.
