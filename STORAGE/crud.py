from db_app1 import db, ResearchCenter

#  CREATE


new_center_3 = ResearchCenter("Biologic Electron Spherome",
                              "Carlos Gardel, PhD", "ksu.edu/bes", 'eng', 66000, 'We do biologic electron stuff', True)
new_center_4 = ResearchCenter("Ceramic Endocronic Synthesis Lab",
                              "Simeon Palestrino, PhD", "ksu.edu/cesl", 'vet', 92300,'We do ceramic endocronic stuff', True)
db.session.add(new_center_3)
db.session.add(new_center_4)
db.session.commit()

# READ

#list of all centers:
all_centers = ResearchCenter.query.all()
print('11111111')
print(all_centers)
print('22222222')

center_2 = ResearchCenter.query.get(2)
if center_2:
    print(center_2.name)
    print(center_2.director)
    print(center_2.url)
else:
    print('There is no id=2')

bioElecSphere = ResearchCenter.query.filter_by(name="Biologic Electron Spherome")
print('3333333333')
print(bioElecSphere.all())

# UPDATE

center_2 = ResearchCenter.query.get(2)
if center_2:
    center_2.budget = 543000
    db.session.add(center_2)
    db.session.commit()

# DELETE

center_1 = ResearchCenter.query.get(1)
if center_1:
    db.session.delete(center_1)
    db.session.commit()

# Where are we now?:
all_centers = ResearchCenter.query.all()
print('44444444444')
print(all_centers)
