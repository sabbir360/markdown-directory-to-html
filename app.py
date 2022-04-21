import mistletoe
import os
from flask import Flask, render_template

app = Flask(__name__)

DOC_DIRECTORY = f'{os.getcwd()}{os.sep}doc'
MARKDOWN_LIST = []
GENERATED = False


def generate_link(file_with_path, file):
    current_path = file_with_path.replace(DOC_DIRECTORY, "").split(os.sep)
    link = dict(name=file, path=file_with_path.replace(DOC_DIRECTORY, ""), depth=current_path)
    MARKDOWN_LIST.append(link)


def read_directory():
    global GENERATED
    if GENERATED is False:
        for root, dirs, files in os.walk(DOC_DIRECTORY):
            for file in files:
                if file.lower().endswith(".md"):
                    # print(os.path.join(root, file))
                    generate_link(os.path.join(root, file), file)
        GENERATED = True


# GENERATE FILE
# read_directory()


@app.route('/')
def index():
    print(MARKDOWN_LIST)
    r = 'Nothing to render.'
    with open('./README.md', 'r') as f:
        r = mistletoe.markdown(f)
        print(r)
    return render_template('index.html', data=r, markdown_list=MARKDOWN_LIST)


if __name__ == '__main__':
    app.run()
