import csv

with open(file='exp_contacts.csv', mode='w', newline='') as csv_file:
    field_names = ['Name', 'Species']
    dict_writer = csv.DictWriter(csv_file, field_names)

    dict_writer.writeheader()
    dict_writer.writerow({'Name': 'Frodo', 'Species': 'Hobbit'})
    