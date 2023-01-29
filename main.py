from flask import Flask
from application.app import app

main_app = Flask(__name__)

main_app.register_blueprint(app, url_prefix='/home')
main_app.config["APPLICATION_ROOT"] = "/home"

if __name__ == "__main__":
    main_app.run(debug=True)
