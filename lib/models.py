from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    company = relationship('Company', backref=backref('freebies', cascade='all, delete-orphan'))
    dev = relationship('Dev', backref=backref('freebies', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<Freebie {self.item_name} | Value: {self.value}>'

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"


Company.devs = relationship(
    'Dev',
    secondary='freebies',
    primaryjoin='Company.id == Freebie.company_id',
    secondaryjoin='Dev.id == Freebie.dev_id',
    viewonly=True,
    backref='companies'
)

def give_freebie(self, dev, item_name, value):
    from models import Freebie  # to avoid circular import if ever split
    return Freebie(item_name=item_name, value=value, company=self, dev=dev)

def oldest_company(cls, session):
    return session.query(cls).order_by(cls.founding_year.asc()).first()

Company.give_freebie = give_freebie
Company.oldest_company = classmethod(oldest_company)

def received_one(self, item_name):
    return any(f.item_name == item_name for f in self.freebies)

def give_away(self, dev, freebie):
    if freebie in self.freebies:
        freebie.dev = dev
        return True
    return False

Dev.received_one = received_one
Dev.give_away = give_away
