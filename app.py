#!/usr/bin/env python

# imports
from flask import Flask, render_template
import yaml
import json

app = Flask(__name__) # Initialize flask

# Read model and config file
config_file = open('config.yaml')
config = yaml.load(config_file, Loader=yaml.FullLoader)
posts_reader = open('models/posts.json')
posts = json.loads(posts_reader.read())

@app.route("/")
def hello():
    return render_template('index.html', blog_title=config['blog_name'], posts=posts)

if __name__ == '__main__':
    app.run(debug=True)