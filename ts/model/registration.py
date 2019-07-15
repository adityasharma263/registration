# -*- coding: utf-8 -*-
from ts import db
from ts.model.base import Base


class Application(Base):

    __tablename__ = 'applications'

    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    department = db.Column(db.String, nullable=True)
    post = db.Column(db.String, nullable=True)
    experience = db.Column(db.String, nullable=True)
    qualification = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    landmark = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    college_name = db.Column(db.String, nullable=True)
    referral = db.Column(db.String, nullable=True)
    resume = db.Column(db.String, nullable=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name
