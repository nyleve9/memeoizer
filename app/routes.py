from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Memeoizer - A Picture Is Worth A Thousand Words"


@app.route('/upload')
def upload_page():
    return "GET the upload form"

