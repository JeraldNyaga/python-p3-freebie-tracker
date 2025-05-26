#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie, Base

# Connect to your database
engine = create_engine("sqlite:///app.db")  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Optional: Clear old data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

# Seed companies
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="CodeWorks", founding_year=1995)

# Seed devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Seed freebies
freebie1 = Freebie(item_name="T-shirt", value=10, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Mug", value=5, company=company2, dev=dev1)
freebie3 = Freebie(item_name="Sticker", value=1, company=company2, dev=dev2)

# Add everything to session and commit
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("✅ Seed data created.")
