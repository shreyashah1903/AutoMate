import flask
from flask_cors import CORS, cross_origin

from main import readEmails
from dotenv import load_dotenv

load_dotenv()


app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config.from_pyfile('settings.py')
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route('/jobs', methods=['GET'])
def fetch_jobs():
    return readEmails()

if __name__ == '__main__':
    app.run()
