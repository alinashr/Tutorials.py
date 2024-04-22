# Write to csv using DictWriter : Python tutorial 226

from csv import DictWriter
with open('zalina.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['name','country'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'name':'alina',
        'country':'Nepal',
    })
    csv_writer.writerow({
        
        'name':'Aliza',
        'country':'India',
    })

    csv_writer.writerows([
        {'name':'alia','country':'china'},
        {'name':'lucky','country':'US'}
    ])




