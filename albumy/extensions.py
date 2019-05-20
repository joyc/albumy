# -*- coding: utf-8 -*- 
""" 
@author: hython 
@license: MIT 
@file: extensions.py 
@time: 2019/05/20
@contact: hython4@gmail.com
@site:  
@software: PyCharm 
"""
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
