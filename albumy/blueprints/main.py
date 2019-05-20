# -*- coding: utf-8 -*- 
""" 
@author: hython 
@license: MIT 
@file: main.py 
@time: 2019/05/20
@contact: hython4@gmail.com
@site:  
@software: PyCharm 
"""
from flask import render_template, Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/explore')
def explore():
    return render_template('main/explore.html')
