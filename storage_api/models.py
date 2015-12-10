from storage_api import db
from sqlalchemy import Column


class Scene(db.Model):
    __tablename__ = 'scene'

    scene_id = Column(db.String, primary_key=True)
    bundle_size = Column(db.Integer)
    bundle_hash = Column(db.String)
    bundle_url = Column(db.String)

    def __repr__(self):
        return "<Scene(scene_id='%s' bundle_size='%s')>" % (
            self.scene_id, self.bundle_size)

    @property
    def serialize(self):
        return {
            'scene_id': self.scene_id,
            'bundle_size': self.bundle_size,
            'bundle_url': self.bundle_url,
            'bundle_hash': self.bundle_hash
        }
