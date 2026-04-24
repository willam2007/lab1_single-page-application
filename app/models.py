from .extensions import db


class TypeBuilding(db.Model):
    __tablename__ = "type_building"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    structures = db.relationship("Structure", back_populates="type")


class Structure(db.Model):
    __tablename__ = "structure"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    height = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey("type_building.id"), nullable=False)

    type = db.relationship("TypeBuilding", back_populates="structures")