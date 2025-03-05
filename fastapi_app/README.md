**FastAPI Application**

This folder contains a simple FastAPI application with a GET endpoint that returns a predefined dictionary with at least five attributes.

Requirements
	•	Python 3.x installed
	•	pip (Python package manager) installed

Installation

**1. Clone the Repository**

git clone <repository-url>
cd <repository-folder>/fastapi_app

**2. Create a Virtual Environment**

python -m venv venv

# On macOS/Linux
source venv/bin/activate   

# On Windows
venv\Scripts\activate     

**3. Install Dependencies**

Run the following command to install the required dependencies:

pip install -r requirements.txt

**Running the API**

To start the FastAPI server, run:

uvicorn main:app --reload

This will start the server at http://127.0.0.1:8000/home
