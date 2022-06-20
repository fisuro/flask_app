from core import app
from core.models import db
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True, port=8080, threaded=True)