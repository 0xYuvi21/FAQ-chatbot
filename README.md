# College FAQ ChatBot (RAG)

A simple yet powerful Retrieval-Augmented Generation (RAG) chatbot built with FastAPI and Python, designed to provide accurate information about SRM Madurai College of Engineering and Technology. The chatbot leverages the Groq API for fast LLM inference and a local JSON file as its knowledge base.

# Features:
College Information Retrieval: Answers questions based on detailed information loaded from college_info.json.

Groq API Integration: Utilizes Groq's high-speed inference engine for fast and efficient LLM responses.

FastAPI Backend: A robust and performant API built with FastAPI, featuring:

Automatic request body validation using Pydantic.

Asynchronous request handling for concurrency.

CORS middleware for seamless frontend integration.

Simple Frontend: A basic HTML/JavaScript interface for user interaction.

Retrieval-Augmented Generation (RAG): Grounds LLM responses in specific, provided college data.


# Tech Stack:
  *Backend:*

    Python 3.9+

    FastAPI

    Pydantic

    Requests

    Uvicorn (ASGI server)

    Groq API (for LLM inference)

  *Frontend:*

    HTML5

    CSS3

    JavaScript (Fetch API, DOM manipulation)

Prerequisites
  * Python 3.9+ installed.

  * pip (Python package installer).

  * A Groq API Key. You can obtain one from Groq Console.
