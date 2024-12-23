# Step 1: Use an official Python runtime as the base image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install fastapi
# Step 5: Install uvicorn explicitly (just in case it's not installed)
RUN pip install --no-cache-dir uvicorn

# Step 6: Confirm uvicorn is installed and available in the PATH
RUN which uvicorn

# Step 7: Expose the port that FastAPI will run on
EXPOSE 8080

# Step 8: Run the FastAPI app with uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
