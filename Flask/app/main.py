from flask import jsonify

from errors import ApiException
from views import AdsView, UserView
from app import get_app

app = get_app()

@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({"status": "error", "description": error.message})
    response.status_code = error.status_code
    return response

def home_page():
    return jsonify({'status': 'REST ADS'})

app.add_url_rule('/', view_func=home_page, methods=['GET'])
app.add_url_rule('/ads/<int:ads_id>', view_func=AdsView.as_view('ads'),  methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ads', view_func=AdsView.as_view('ads_create'),  methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view("user"), methods=["GET", "PATCH", "DELETE"])
app.add_url_rule('/users', view_func=UserView.as_view('users_create'), methods=['POST'])

app.run()