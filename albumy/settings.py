# -*- coding: utf-8 -*- 
""" 
@author: hython 
@license: MIT 
@file: settings.py 
@time: 2019/05/20
@contact: hython4@gmail.com
@site:  
@software: PyCharm 
"""
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


class BaseConfig:
    ALBUMY_ADMIN_EMAIL = os.getenv('ALBUMY_ADMIN', 'admin@hython.com')
    ALBUMY_PHOTO_PER_PAGE = 12
    ALBUMY_COMMENT_PER_PAGE = 15
    ALBUMY_NOTIFICATION_PER_PAGE = 20
    ALBUMY_USER_PER_PAGE = 20
    ALBUMY_MANAGE_PHOTO_PER_PAGE = 20
    ALBUMY_MANAGE_USER_PER_PAGE = 30
    ALBUMY_MANAGE_TAG_PER_PAGE = 50
    ALBUMY_MANAGE_COMMENT_PER_PAGE = 30
    ALBUMY_SEARCH_RESULT_PER_PAGE = 20
    ALBUMY_MAIL_SUBJECT_PREFIX = '[Albumy]'

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024  # file size exceed to 3 Mb will return a 413 error response.

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Albumy Admin', MAIL_USERNAME)


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = \
        prefix + os.path.join(basedir, 'data-dev.db')
    REDIS_URL = "redis://localhost"


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
