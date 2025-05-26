#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie, Base

# This is the connection to my database
engine = create_engine("sqlite:///app.db")  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# Tech companies
company1 = Company(name="Safaricom coders", founding_year=1920)
company2 = Company(name="Waters Snakes", founding_year=2021)
company3 = Company(name="TechieNiBaddie", founding_year=2020)

# Competing devs
dev1 = Dev(name="Anna")
dev2 = Dev(name="Barbara")
dev3 = Dev(name="Jamo")
dev4 = Dev(name="Kevin")
dev5 = Dev(name="Kloppo")

# Seed freebies
freebie1 = Freebie(item_name="T-shirt", value=7, company=company3, dev=dev1)
freebie2 = Freebie(item_name="Mug", value=4, company=company2, dev=dev1)
freebie3 = Freebie(item_name="Sticker", value=1, company=company3, dev=dev2)
freebie4 = Freebie(item_name="Gaming Mouse", value=6, company=company3, dev=dev3)
freebie5 = Freebie(item_name="Hoodie", value=5, company=company1, dev=dev2)
freebie6 = Freebie(item_name="Coffee maker", value=9, company=company1, dev=dev4)
freebie6 = Freebie(item_name="Hat", value=9, company=company2, dev=dev5)

# Add everything to session and commit
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("✅ Seed data created.")
