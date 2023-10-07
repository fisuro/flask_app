from core import app
from core.models import db

if __name__ == "__main__":
    # with app.app_context():

    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True, host="0.0.0.0")
