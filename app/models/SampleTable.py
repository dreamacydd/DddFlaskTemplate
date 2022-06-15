"""Sample table for the Flask sample app.

William Ellison
<wae@dreamacy.io>
June 2022
"""
from . import db

class SampleTable(db.Model):
    __tablename__ = "sample"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(90), nullable=False)
    
    def __init__(self, name: str):
        self.name = name
    
    def json_serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }
