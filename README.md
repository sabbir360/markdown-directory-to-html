# Markdown to HTML Website/Documents

## Introduction
To ease the use of markdown and browse those hard written contents on browser its a little effort.

This system can display a nicely formatted HTML for your markdown with simplicity.

### Demo
![Demo of this project](./doc/Markdown%20directory%20to%20html%20demo.gif)

## How to use
To use this, simply put all your markdown, whether it's multi directory or single to the **doc** folder.
Then run this project, either using Docker or, Flask. Boom!

## How to run this project
I would recommend using docker, but if you want to run using Flask built-in server. Follow this steps
  - **For Mac/linux/Ubuntu**
     - [Install python 3.7+](https://realpython.com/installing-python/)
     - Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
     - Clone this project  `git clone https://github.com/sabbir360/markdown-directory-to-html.git`
     - Install virtualenv `pip3 install virtualenv`
     - `cd markdown-directory-to-html` and Create a virtualenv `virtualenv .env`
     - Load virtualenv `source .env/bin/activate`
     - Install required package `pip3 install -r requirements`
     - Copy your markdown directory and files at **doc** folder. 
     - Run it `python app.py` and browse `127.0.0.1:5000`
  - **For windows**
    - [Install python 3.7+](https://realpython.com/installing-python/)
    - Install [Git](https://git-scm.com/download/win)
    - Clone this project  `git clone https://github.com/sabbir360/markdown-directory-to-html.git`
    - Install virtualenv `pip install virtualenv`
    - `cd markdown-directory-to-html` and Create a virtualenv `virtualenv venv`
    - Load virtualenv `venv\Script\activate`
    - Install required package `pip install -r requirements`
    - Copy your markdown directory and files at **doc** folder. 
    - Run it `python app.py` and browse `127.0.0.1:5000`

If you want to avoid these hassles, Install 
 - Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
 - [Docker](https://docs.docker.com/engine/install/).
 - [Docker Compose](https://docs.docker.com/compose/install/)
 - Clone this project  `git clone https://github.com/sabbir360/markdown-directory-to-html.git`
 - `cd markdown-directory-to-html` 
 - `docker-compose build` and then `docker-compose up -d`
 - Browse `127.0.0.1:5000`
 - To remove this from docker `docker-compose down`

## How to run unittest
- Inside your virtualenv run `python -m unittest discover tests`

## Limitation / future plan
  - This project has some error for unwanted Markdown format
  - For linking any internal directories
  - Those will be solved in the future, or you can raise issue or, contact me