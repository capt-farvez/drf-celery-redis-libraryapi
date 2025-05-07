# Steps to Install Redis Using Docker:

### 1. Install Docker Desktop:

- Download and install Docker Desktop from here.
- Follow the installation steps and start Docker after installation.

### 2. Run Redis in Docker:

- Once Docker is running, open a terminal (Command Prompt, PowerShell, or Git Bash) and run the following command to start Redis:

``` 
docker run --name redis -p 6379:6379 -d redis 
```
- This command will pull the Redis image from Docker Hub and run Redis on port 6379.

### 3. Verify Redis:

- To check if Redis is running correctly, you can open another terminal and run:
```
docker exec -it redis redis-cli ping
```
- You should see the output PONG, confirming that Redis is running.

### 4. Use Redis in Django:

- In your Django project, make sure that the Redis connection is pointing to localhost (or 127.0.0.1).
- Redis will be running on port 6379 by default.