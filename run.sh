FLASK_APP="app"
FLASK_DEBUG="True"

export env=$env:$FLASK_APP:$FLASK_DEBUG

flask run --host=0.0.0.0