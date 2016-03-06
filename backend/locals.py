import re

DB = {'host': '173.194.246.10', 'user': 'magdalena', 'password': 'root', 'db': 'kickstarter'}
_INSTANCE_NAME = 'kickstarter-dev:kickstarter-sql'
PROPERTIES = {'socket': '/cloudsql/%s' %_INSTANCE_NAME, 'db': 'kickstarter', 'user': "root"}


def escape(string):
    re.sub(r'(\-|\]|\^|\$|\*|\.|\\)', lambda m: {'-': '\-', ']': '\]', '\\': '\\\\', '^': '\^', '$': '\$', '*': '\*', '.': '\.'}[m.group()], string)


def undo_escape(string):
    re.sub(r'(\\\-|\\\]|\\\^|\\\$|\\\*|\\\.|\\\\)', lambda m: {'\-': '-', '\]': ']', '\\\\': '\\', '\^': '^', '\$': '$', '\*': '*', '\.': '.'}[m.group()], string)
