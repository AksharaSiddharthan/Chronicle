# Chronicle
Tech Stack

This project uses a modern full-stack architecture combining React, FastAPI, and a fine-tuned NLP model for intelligent journal entry classification.

Frontend

* **React**: Core library for building responsive user interfaces
* **Tailwind CSS**: Utility-first styling for a clean, consistent UI
* **Recharts**: For visualizing category distribution using pie charts
* **react-calendar**: Calendar component for filtering entries by date
* **Fetch API**: Used to communicate with the FastAPI backend

Backend

* **FastAPI**: High-performance Python web framework for building REST APIs
* **Uvicorn**: ASGI server for running FastAPI in development and production
* **Pydantic**: Handles data validation and schema enforcement
* **SQLAlchemy**: ORM used for database interactions
* **SQLite**: Lightweight relational database for storing entries

Machine Learning

* **Hugging Face Transformers** (e.g., BERT or DistilBERT): NLP model used to classify journal entries into categories like Nutrition, Exercise, Soul, etc.
* **scikit-learn**: Assists with preprocessing and evaluation
* **safetensors**: Used for efficient and secure model serialization




