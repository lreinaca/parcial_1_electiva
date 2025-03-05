**Database Setup with Docker**

This folder contains the necessary files to set up a database inside a Docker container using docker-compose.

Requirements
	•	Docker installed on your system
	•	docker-compose installed

Configuration

The database is configured to:
	•	Run inside a Docker container
	•	Expose port 4500
	•	Be defined using docker-compose.yml

How to Run the Container

**1. Clone the repository**

git clone <repository-url>
cd <repository-folder>/Docker

**2. Start the Database Container**

Run the following command to start the database:

docker-compose up -d

This will:
-Pull the necessary database image (if not available)
-Create the container
-Expose the database on port 4500

**3. Verify the Running Container**

Check if the database container is running:

docker ps

You should see a container with the exposed port 4500.

**4. Stop and Remove the Container**

If you need to stop the database:

docker-compose down