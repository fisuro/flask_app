from core import app
from core.models import db
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)