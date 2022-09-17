import os

from flask import Flask, abort, render_template, request

from data_service import do_command
from utils import get_file_lines

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/")
def main_page():
    filenames = os.listdir(DATA_DIR)
    return render_template("form.html", filenames=filenames)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        file_name = request.form["file_name"]
        cmd1 = request.form["cmd1"]
        value1 = request.form["value1"]
        cmd2 = request.form["cmd2"]
        value2 = request.form["value2"]
        
        file_path = os.path.join(DATA_DIR, file_name)
        lines = get_file_lines(file_path)
    except KeyError:
        abort(400)
    except FileExistsError as e:
        abort(400, e)
    
    try:
        lines = do_command(lines, cmd1, value1)
        lines = do_command(lines, cmd2, value2)
    except ValueError as e:
        abort(400, e)
    
    return app.response_class("\n".join(lines), content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
