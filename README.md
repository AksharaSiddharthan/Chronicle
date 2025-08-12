# Chronicle
Tech Stack
Chronicle is a digital journaling and self-assessment app that lets you log daily activities like journal entries and automatically generates insights about your performance in different areas of life. Instead of just keeping notes, Chronicle structures your reflections into measurable categories — helping you visualise your growth over time.


**Features**
Daily Journal Logging – Write free-form entries about your day, events, and thoughts. <br>
Category-Based Tracking – Rate or tag your activities in areas such as: <br>
*Health & Fitness <br>
*Learning & Skills<br>
*Work & Productivity<br>
*Social & Relationships<br>
*Creativity & Hobbies<br>
*Mindset & Wellbeing<br>
*Automated Analysis – Summarises how you’ve been doing in each category based on your logs.<br>
*Data Visualisation – Provides weekly or monthly charts of your performance.<br>
*Search & Filter – Find past entries by category, date, or keyword.<br>
*Export & Backup – Save your data securely in JSON or CSV format.<br>

-------

# Tech Stack
This project uses a modern full-stack architecture combining React, FastAPI, and a fine-tuned NLP model for intelligent journal entry classification.

Frontend

* **React**: Core library for building responsive user interfaces
* **Tailwind CSS**: Utility-first styling for a clean, consistent UI
* **Recharts**: For visualising category distribution using pie charts
* **react-calendar**: Calendar component for filtering entries by date
* **Fetch API**: Used to communicate with the FastAPI backend

Backend

* **FastAPI**: High-performance Python web framework for building REST APIs
* **Uvicorn**: ASGI server for running FastAPI in development and production
* **Pydantic**: Handles data validation and schema enforcement
* **SQLAlchemy**: ORM used for database interactions
* **SQLite**: Lightweight relational database for storing entries

Machine Learning

* **Hugging Face Transformers**: The NLP model is used to classify journal entries like Nutrition, Exercise, Soul, etc.
* **scikit-learn**: Assists with preprocessing and evaluation
* **safetensors**: Used for efficient and secure model serialisation




