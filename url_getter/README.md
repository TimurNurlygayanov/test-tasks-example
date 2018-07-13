Introduction
------------
This folder contain example of web crawler with Python3 asyncio library.

The code is organaized as client-server application, with distribution of crawler tasks 
by all available agents. 

How To Run
----------
To run the crawler:

 - Run server:


    python3 crawler_server.py

    
 - Run agents (can be started on many different nodes):


    bash run_agents.sh


 - Open http://0.0.0.0:5000 and upload ZIP file with the list of requests
