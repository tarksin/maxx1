from db_app1 import db, ResearchCenter

# Model -> tables
db.create_all()

new_center_1 = ResearchCenter("Numeric Resonant Arthropod Lab", "Genevieve Flaubert, PhD","ksu.edu/nral", 'bio', 34000,'We do numeric resonant stuff' ,True)
new_center_2 = ResearchCenter("Magnetic Genome Accelerator", "Maxim Svoboda, PhD","ksu.edu/mga", 'eng', 17500, 'We do magnetic genome stuff',False)

print(new_center_1.id)
print(new_center_2.id)

# db.session.add_all([new_center_1, new_center_2])    OR:
db.session.add(new_center_1)
db.session.add(new_center_2)

db.session.commit()

print(new_center_1.id)
print(new_center_2.id)
