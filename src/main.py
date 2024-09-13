from fastapi import FastAPI

app = FastAPI()

# Use the app instance of the FastAPI class
# to handle an HTTP route & HTTP method
@app.get("/")
def read_index():
    """
    Return a Python Dictionary that supports JSON serialization
    """
    return {"Hello": "World"}

@app.get("/api/v1/hello-world/")
def read_hello_world():
    """
    Return an API response...
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}

@app.get("/api/v1/welcome/")
def read_welcome():
    """
    Return PhunkyTech welcome message.
    """
    return {"Greeting": "Welcome to PhunkyTech Ltd!"}
