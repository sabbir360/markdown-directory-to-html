import mistletoe
import os
from flask import Flask, render_template, request, abort

DOC_DIRECTORY = f'{os.getcwd()}{os.sep}doc'


def directory_tree(path):
    string_build = ""
    space = "&nbsp;&nbsp;&nbsp;"

    for dirpath, dirnames, filenames in os.walk(path):
        directory_level = dirpath.replace(path, "")
        directory_level = directory_level.count(os.sep)

        if directory_level == 0:
            root_display = 'style="display: inline!important"'
            alter_display = 'style="display: none!important"'

            dir_name = f"{dirpath.split(os.sep)[-1]}"
            dir_sanitized = dirpath.replace(DOC_DIRECTORY, "")
            dir_id = dir_sanitized.replace(os.sep, "_")
        else:
            root_display = ""
            alter_display = ''

            dir_name = os.path.basename(dirpath)
            dir_sanitized = dirpath.replace(DOC_DIRECTORY, "")
            dir_id = dir_sanitized.replace(os.sep, "_")

        indent = space * (4 * directory_level)
        indent_2 = space * (4 * directory_level + 1)

        string_build += f'''
            <div data-id="{dir_id}" class="directory-wrapper">
                {indent}
                <span class="directory-close" {root_display}>📁&nbsp;</span>
                <span class="directory-open" {alter_display}>📂&nbsp;</span>
                <strong>{dir_name}</strong>/            
            <div id="{dir_id}" class="directory-child" {root_display}>
        '''

        for f in filenames:

            if f.endswith(".md"):

                if directory_level == 0 and f == "README.md":
                    menu = " menu-selected"
                    select_id = ''
                else:
                    menu = ""
                    select_id = f'{dir_id}__sep__{f.replace(".md", "")}'
                string_build += f'''
                <div>
                    &nbsp;&nbsp;{indent_2}                    
                    <a class="section-link{menu}" 
                    id="{select_id}" 
                    href="?dir={dir_sanitized}&file={f}#{select_id}"> 
                        <span>🗎&nbsp;</span>{f}
                    </a>            
                </div>'''

        string_build += "</div></div>"

    return f"<div>{string_build}</div>"


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
