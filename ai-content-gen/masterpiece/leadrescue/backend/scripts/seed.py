from app import db
from app.models import BusinessProfile

engine = db.init_db()
session = db.get_session()
profile = BusinessProfile(name="Demo Service", services="plumbing", review_link="https://g.page/r/demo")
session.add(profile)
session.commit()
session.close()
print('Seeded business profile')
