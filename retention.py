import app
from datetime import timedelta
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(app)

def retention_date():
    app.iptofingerprintsModel.query.all()
    retention_timestamp = datetime.datetime.now() - timedelta(minutes=1)
    print(retention_timestamp)
    check_date_iptofingerprints = app.iptofingerprintsModel.query.filter(app.iptofingerprintsModel.timestamp <= retention_timestamp).all()
    for fingerprint in check_date_iptofingerprints:
        print(fingerprint.id)
        app.iptofingerprintsModel.query.filter_by(id=fingerprint.id).delete()
    print(check_date_iptofingerprints)
    app.cookietofingerprintModel.query.all()
    app.db.session.commit()


# scheduler = BackgroundScheduler()
# scheduler.add_job(func=retention_date, trigger="interval", seconds=100, max_instances=1)
# scheduler.start()
# atexit.register(lambda: scheduler.shutdown())