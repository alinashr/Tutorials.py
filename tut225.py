

from csv import writer
with open('zalina.csv','w',newline='') as f:
    # next
    csv_writer=writer(f)
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['Alina','Nepal'])
    # csv_writer.writerow(['Harry','US'])
    csv_writer.writerows([['name','country'],['Alina','Nepal'],['Harry','US']])



