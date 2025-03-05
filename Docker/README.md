**-Running the Database Container**

To start the container, run the following command in the root directory of the project:

docker-compose up -d

This will pull the necessary Docker image, create the container, and run it in the background.

**-to verify the Database**

You can check if the database container is running properly by executing:

docker-compose ps

This should show the database container with the exposed port 4500.

