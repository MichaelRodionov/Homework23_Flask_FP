from flask import Flask, abort, request
import os

from utils.implemented import validator
from utils.constants import DATA_DIR
from classes.user_request import UserRequest


# ----------------------------------------------------------------
def create_app() -> Flask:
    """
    Function to create our application
    :return: application
    """
    application = Flask(__name__)
    return application


app = create_app()


@app.route("/perform_query/", methods=['POST', 'GET'])
def perform_query():
    """
    Route to form request by query string (keys - filename, cmd1, cmd2, value1, value2)
    :return: response with overwritten data
    """
    args = request.values

    if validator.is_correct(args):
        file_path = os.path.join(DATA_DIR, args.get('filename'))

        if validator.check_file_exists(file_path):
            user_request = UserRequest(args)

            with open(file_path, encoding='utf8') as f:
                result = '\n'.join(user_request.get_result(f))
        else:
            abort(400, 'File not found')
    else:
        abort(400, 'Arguments problem')
    return app.response_class(result, content_type="text/plain")


if __name__ == '__main__':
    app.run()

