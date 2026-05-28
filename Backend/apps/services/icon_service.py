from apps.models import Icon


def list_icons(db):
    return db.query(Icon).all()


def get_icon(db, icon_id):
    return db.query(Icon).filter(Icon.id == icon_id).first()
