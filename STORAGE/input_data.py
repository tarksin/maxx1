from models import db, Center, Staffer, Project

new_center_1 = Center("Numeric Resonant Arthropod Lab", "Genevieve Flaubert, PhD","ksu.edu/nral", 'bio', 34000, 'We do numeric resonant stuff', 'laptop1.jpg', True)
new_center_2 = Center("Magnetic Genome Accelerator", "Maxim Svoboda, PhD","ksu.edu/mga", 'eng', 17500, 'We do magnetic genome stuff', 'laptop2.jpg', False)
new_center_3 = Center("Biologic Electron Spherome", "Carlos Gardel, PhD", "ksu.edu/bes", 'eng', 66000, 'We do biologic electron stuff', 'laptop3.jpg', True)

db.session.add_all([new_center_1, new_center_2, new_center_3])
db.session.commit()

print(Center.query.all())

center_2 = Center.query.filter_by(url='ksu.edu/mga').first()

staffer_1 = Staffer('Maria', 'Gentry', 'M.S.', 'Associate Director', 'Associate Director', center_2.id)
staffer_2 = Staffer('Quioqui', 'Manheim', 'PhD', 'Assistant Professor', 'Adjunct Director', center_2.id)
staffer_3 = Staffer('Penelope', 'Thrash', 'M.S.', 'Technician', 'Technician', center_2.id)
db.session.add(staffer_1)
db.session.add(staffer_2)
db.session.add(staffer_3)
db.session.commit()
db.session.refresh(staffer_1)
db.session.refresh(staffer_2)
db.session.refresh(staffer_3)


project_1 = Project('National Research Project X', staffer_1.id)
project_2 = Project('National Research Project Y', staffer_1.id)
project_3 = Project('National Research Project Z', staffer_1.id)

db.session.add_all([project_1, project_2, project_3])
db.session.commit()

center_x = Center.query.filter_by(url='ksu.edu/mga').first()

print(center_x)

print(center_x.report_staffers())
