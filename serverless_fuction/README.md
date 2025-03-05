**Serverless Function in Python**

This folder contains a serverless function implemented in Python that returns a personalized greeting. The function is designed to be deployed using Serverless Framework.

Requirements
	•	Node.js installed (for Serverless Framework)
	•	Serverless Framework installed (npm install -g serverless)
	•	AWS CLI configured (or another cloud provider)

Installation and Setup

**1. Clone the Repository**

git clone <repository-url>
cd <repository-folder>/serverless_function

**2. Install Serverless Framework**

npm install -g serverless

**3. Install Python Dependencies**

If the function has additional dependencies, install them inside a virtual environment:

python -m venv venv

# On macOS/Linux
source venv/bin/activate   

# On Windows
venv\Scripts\activate      

pip install -r requirements.txt

**4. Run Serverless Offline**

serverless offline --stage dev

This will start a local server, and you can access the function at:

http://localhost:3000/hello
