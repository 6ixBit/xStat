from app import app
from app.routes import dash_app1

# Run dash app instance
if __name__ == "__main__":
    dash_app1.run_server(host='0.0.0.0', port=80, debug=True)