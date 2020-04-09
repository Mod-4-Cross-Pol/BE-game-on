import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# db = SQLAlchemy(app)
print(os.environ['APP_SETTINGS'])

@app.route('/')
@app.route('/api/v1')
def home_page():
  return "Honey I'm home and I have an API"



if __name__ == '__main__':
    app.run()
