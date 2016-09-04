from flask import Flask
from flask import (abort,
                   make_response,
                   redirect,
                   render_template,
                   request,
                  )
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template ('/data_graph.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
