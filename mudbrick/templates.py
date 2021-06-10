#frontend modules
base_file = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% include 'styles.html' %}
    
    {% block title  %}{% endblock %}
</head>
<body>
    {% block content  %}
    {% endblock %}
</body>
</html>
"""

index_file = """{% extends 'base.html' %}

{% block title %}
    <title> Mudbrick </title>
{% endblock  %}

{% block content %}
<div class="text">
    <h1>MUDBRICK</h1>
    <br>
    <p>A Flask extension that automatically builds a boilerplate template for your web application backend by
using a simple cli command. It builds a modular architecture that's manageable and easily deployable. 
Don't worry about configuring and structuring your application factory pattern from scratch. Mudbrick
does that for you.
    </p>
    <br>
    <h5>Created by: Owen O. Phakade</h5>
</div>

<div class="container">
    <div class="glowing">
        <span style="--i:1;"></span>
        <span style="--i:2;"></span>
        <span style="--i:3;"></span>
    </div>
    <div class="glowing">
        <span style="--i:1;"></span>
        <span style="--i:2;"></span>
        <span style="--i:3;"></span>
    </div>
    <div class="glowing">
        <span style="--i:1;"></span>
        <span style="--i:2;"></span>
        <span style="--i:3;"></span>
    </div>
    <div class="glowing">
        <span style="--i:1;"></span>
        <span style="--i:2;"></span>
        <span style="--i:3;"></span>
    </div>
</div>

{% endblock  %}
 
"""

styles_file = """<style>
    *{
        margin: 0;
        padding: 0;
    }

    body{
        background: #000;
        overflow: hidden;
    }

    .container{
        display: flex;
        justify-content: center;
        align-items: center; 
        width: 100%;
        min-width: 100vh;
    }

    .text{
        color: white;
        padding-top: 150px;
        padding-right: 300px;
        padding-left: 50px; 
        animation: shake 2.5s  ease infinite;
    }

    @keyframes shake{

       0%, 100%{
           transform: translateY(-3px)
       }
       50%{
           transform: translateY(2px)
       } 
    }

    .text h1{
        color: teal;
    }

    .glowing{
        position: relative;
        min-width: 600px;
        height: 600px;
        margin: -150px;
        transform-origin: right;
        animation: colorchange 5s linear infinite;
    }

    @keyframes colorchange {
        0%{
            filter: hue-rotate(0deg);
            transform: rotate(0deg);
        }
        100%{
            filter: hue-rotate(360deg);
            transform: rotate(360deg);
        }
    }

    .glowing:nth-child(even){
        transform-origin: left;
    }

    .glowing span{
        position: absolute;
        top: calc(80px * var(--i) );
        left: calc(80px * var(--i) );
        bottom: calc(80px * var(--i) );
        right: calc(80px * var(--i) );
    }

    .glowing span:before{
        content: '';
        position: absolute;
        top: 50%;
        left: -8px;
        width: 15px;
        height: 15px;
        background: #f00;
        border-radius: 50%;
    }
   
    .glowing span:nth-child(3n + 1):before{
        background: rgba(134, 255, 0, 1);
        box-shadow: 0 0 20px rgba(134, 255, 0, 1),
                    0 0 40px rgba(134, 255, 0, 1),
                    0 0 60px rgba(134, 255, 0, 1),
                    0 0 80px rgba(134, 255, 0, 1),
                    0 0 0 8px rgba(134, 255, 0, .1);
    }

    .glowing span:nth-child(3n + 2):before{
        background: rgba(255, 214, 0, 1);
        box-shadow: 0 0 20px rgba(255, 255, 0, 1),
                    0 0 40px rgba(255, 255, 0, 1),
                    0 0 60px rgba(255, 255, 0, 1),
                    0 0 80px rgba(255, 255, 0, 1),
                    0 0 0 8px rgba(255, 255, 0, .1);
    }

    .glowing span:nth-child(3n + 3):before{
        background: rgba(0,226, 255, 1);
        box-shadow: 0 0 20px rgba(0,226, 255, 1),
                    0 0 40px rgba(0,226, 255,  1),
                    0 0 60px rgba(0,226, 255,  1),
                    0 0 80px rgba(0,226, 255, 1),               
                    0 0 0 8px rgba(0,226, 255, .1);
    }

    .glowing span:nth-child(3n + 1){
         animation: animate 10s alternate infinite;
    }

    @keyframes animate {
        0%{
            transform: rotate(0deg);
        }
        100%{
            transform: rotate(360deg);
        }
    }

    .glowing span:nth-child(3n + 2){
         animation: animate-reverse 3s alternate infinite;
    }

    @keyframes animate-reverse {
        0%{
            transform: rotate(360deg);
        }
        100%{
            transform: rotate(0deg);
        }
    }

    .glowing span:nth-child(3n + 3){
         animation: animate-reverse 8s alternate infinite;
    }

    @keyframes animate-reverse {
        0%{
            transform: rotate(360deg);
        }
        100%{
            transform: rotate(0deg);
        }
    }
</style>
"""

#backend modules
wsgi_file = """
app = create_app()

if __name__ == '__main__':
	app.run()
"""
gitignore_file = """instance/*
!instance/.gitignore
.webassets-cache
.env
__pycache__/
*.py[cod]
*$py.class
"""
component_file = """from flask import Blueprint, render_template

component_bp = Blueprint( "component_bp", __name__)

@component_bp.route("/")
def helloworld():
	 return render_template('index.html')
 """

def init_file(project_name):
    init_file = f"""from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_manager="{project_name}.config.BaseConfig"):

    app = Flask(__name__)
    #import configurations
    app.config.from_object(config_manager)

    #initialise extension
    db.init_app(app)

    #Import your blueprints.
    from .component.routes import component_bp

    #register blueprint
    app.register_blueprint(component_bp)

    return app
"""
    return init_file

config_file ="""import os

class BaseConfig:

	DEBUG = True

	ENV = 'Development'

	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SECRET_KEY = os.environ.get("SECRET_KEY")

	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
"""

models_file ="""from . import db

class Model(db.Models):
	id = db.Column(db.Integer, primary_key=True)
	...
"""