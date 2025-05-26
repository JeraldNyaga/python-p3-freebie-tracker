#!/usr/bin/env python3

from sqlalchemy import create_engine
<<<<<<< HEAD

from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    import ipdb; ipdb.set_trace()
=======
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

engine = create_engine("sqlite:///app.db")
Session = sessionmaker(bind=engine)
session = Session()

# Test Dev -> Freebies
alice = session.query(Dev).filter_by(name="Alice").first()
print(f"{alice.name}'s freebies:")
for freebie in alice.freebies:
    print(f"  - {freebie.item_name} from {freebie.company.name}")

# Test Company -> Devs
codeworks = session.query(Company).filter_by(name="CodeWorks").first()
print(f"\nDevs who got freebies from {codeworks.name}:")
for dev in codeworks.devs:
    print(f"  - {dev.name}")

# Test Freebie.print_details
print("\nFreebie details:")
for freebie in session.query(Freebie).all():
    freebie.print_details()

# Test Dev.received_one
print(f"\nHas Alice received a Mug? {alice.received_one('Mug')}")

# Test Dev.give_away
bob = session.query(Dev).filter_by(name="Bob").first()
mug = session.query(Freebie).filter_by(item_name="Mug").first()
alice.give_away(bob, mug)
session.commit()
print(f"\nAfter giveaway, Mug is now owned by {mug.dev.name}")
>>>>>>> 5c45024 (First version of code)
