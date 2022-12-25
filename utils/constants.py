import os

# ----------------------------------------------------------------
# constants for application
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")

QUERY_KEYS = {'filename', 'cmd1', 'value1', 'cmd2', 'value2'}

COMMANDS = {'filter', 'map', 'unique', 'sort', 'limit'}

SORT_PARAMS = {'asc', 'desc'}
