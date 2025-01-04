# Browser Use

This project is a demonstration of using a [browser-use](https://github.com/browser-use/browser-use) as an API. The API can then be invoked manually or using any AI Agent.

## Purpose

The purpose of this project is to provide a browser-use agent as an API service, running in headless mode within a Docker container. This service can be consumed as a tool by AI agents, allowing them to browse the internet and retrieve final responses in natural language for any kind of web automation.

## Setup Instructions

### Running Locally

1.  Ensure you have Python 3.11+ installed.
2.  Clone the repo: `git clone <github URL to this project>`
3.  Create a virtual environment: `python3 -m venv .venv`
4.  Activate the virtual environment: `source .venv/bin/activate`
5.  Install the dependencies: `pip install -r requirements.txt`
6.  Run the server: `python server.py`
7. In another terminal, hit the API entpoint using CURL or any tool like postman or REST client
```
curl -X POST -H "Content-Type: application/json; charset=utf-8" -d '{"task": "go to google  and get me title and responsibilities  of two software engineering jobs in phoenix along with their links"}' http://localhost:5055/v1/query
```

### Running with Docker

1.  Ensure you have Docker installed.
2.  Get into project folder: `cd <project folder>`
3.  Build the Docker image: `docker compose --build`. Once built, subsequently you can run `docker compose up`
3.  In another terminal, hit the API entpoint using CURL or any tool like postman or REST client
```
curl -X POST -H "Content-Type: application/json; charset=utf-8" -d '{"task": "go to google  and get me title and responsibilities  of two software engineering jobs in phoenix along with their links"}' http://localhost:5055/v1/query
```