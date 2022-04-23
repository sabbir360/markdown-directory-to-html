import mistletoe
import os
from flask import Flask, render_template, request, abort
from utils import directory_tree

DOC_DIRECTORY = f'{os.getcwd()}{os.sep}doc'

MARKDOWN_LIST = directory_tree(DOC_DIRECTORY)
app = Flask(__name__)


@app.route('/')
def index():
    directory = request.args.get("dir", "")
    file = request.args.get("file", "")

    if directory.find("..") != -1:
        return abort(403, "This request not allowed.")
    if directory == "":
        directory = DOC_DIRECTORY
    else:
        directory = f"{DOC_DIRECTORY}{directory}"
    if file == "":
        file = "README.md"

    try:
        with open(f'{directory}{os.sep}{file}', 'r') as f:
            r = mistletoe.markdown(f)
    except FileNotFoundError:
        r = 'Please select file from left side tree.'
        print(f"{directory}{file}")

    return render_template('index.html', data=r, markdown_list=MARKDOWN_LIST)


if __name__ == '__main__':
    app.run()
