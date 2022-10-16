import flask

from main import readEmails
from dotenv import load_dotenv

load_dotenv()


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config.from_pyfile('settings.py')


@app.route('/jobs', methods=['GET'])
def fetch_jobs():
    return readEmails()

if __name__ == '__main__':
    app.run()
