from storage_api import db

from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String

class Scene(db.Model):
    __tablename__ = 'scene'

    scene_id = Column(db.String, primary_key=True)
    bundle_size = Column(db.Integer)
    bundle_hash = Column(db.String)
    bundle_url = Column(db.String)

    def __repr__(self):
        return "<Scene(scene_id='%s' bundle_size='%s')>" % (
            self.scene_id, self.bundle_size)
