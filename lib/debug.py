#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

engine = create_engine("sqlite:///app.db")
Session = sessionmaker(bind=engine)
session = Session()

# Test Dev -> Freebies
anna = session.query(Dev).filter_by(name="Anna").first()
print(f"{anna.name}'s freebies:")
for freebie in anna.freebies:
    print(f"  - {freebie.item_name} from {freebie.company.name}")

# Test Company -> Devs
TechieNiBaddie = session.query(Company).filter_by(name="TechieNiBaddie").first()
print(f"\nDevs who got freebies from {TechieNiBaddie.name}:")
for dev in TechieNiBaddie.devs:
    print(f"  - {dev.name}")

# Test Freebie.print_details
print("\nFreebie details:")
for freebie in session.query(Freebie).all():
    freebie.print_details()

# Test Dev.received_one
print(f"\nHas Anna received a Mug? {anna.received_one('Mug')}")

# Test Dev.give_away
jamo = session.query(Dev).filter_by(name="Jamo").first()
mug = session.query(Freebie).filter_by(item_name="Mug").first()
anna.give_away(jamo, mug)
session.commit()
print(f"\nAfter giveaway, Mug is now owned by {mug.dev.name}")
