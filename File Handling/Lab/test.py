import pickle

# def storeData():
#     # initializing data to be stored in db
#     Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
#              'age': 21, 'pay': 40000}
#     Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
#                'age': 50, 'pay': 50000}
#     # database
#     db = {}
#     db['Omkar'] = Omkar
#     db['Jagdish'] = Jagdish
#     # Its important to use binary mode
#     dbfile = open('examplePickle', 'ab')
#     # source, destination
#     pickle.dump(db, dbfile)
#     dbfile.close()
#
#
# def loadData():
#     # for reading also binary mode is important
#     dbfile = open('examplePickle', 'rb')
#     db = pickle.load(dbfile)
#     for keys in db:
#         print(keys, '=>', db[keys])
#     dbfile.close()
#
#
# if __name__ == '__main__':
#     storeData()
#     loadData()

# ANOTHER WAY T+FOR SAME THING:
# Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
#          'age': 21, 'pay': 40000}
# Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
#            'age': 50, 'pay': 50000}
# db = {}
# db['Omkar'] = Omkar
# db['Jagdish'] = Jagdish
# # For storing
# b = pickle.dumps(db)  # type(b) gives <class 'bytes'>
# # For loading
# myEntry = pickle.loads(b)
# print(myEntry)

import csv
#
# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_date']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_date': '05/21/1978'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_date': '03/17/1989'})

import pandas
df = pandas.read_csv('employee_file2.csv', index_col='emp_name', parse_dates=['birth_date'])
print(df)
print(type(df['birth_date'][0]))
df.to_csv('hrdata.csv')