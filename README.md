PhunkyTech Workflow
===================

1. Checks out the code to build an image.
2. Logs in to Docker Hub.
3. Builds container with the Dockerfile.
4. Tags container with relevant tags.
5. Pushes the container(image) to Docker Hub.
6. SSH into the production virtual machine.
7. Verifies Docker is installed; if not, install it. If Docker is not installed, also install Docker Compose.
8. Copies the compose.prod.yaml file to the production virtual machine.
9. Creates a dotenv file (.env) and copies it to the production virtual machine.
10. Pulls the latest container image with docker compose pull.
11. Runs the container with docker compose up -d.
12. Cleans up the SSH connection and dotenv file.
 
