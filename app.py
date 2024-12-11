from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route and function
@app.route('/')
def hello_cloud():
    return 'Hello from Yegbe ECS Container.'

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
