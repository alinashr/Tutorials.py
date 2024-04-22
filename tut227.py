# Read and Write CSV files simultaneously (HINDI)

from csv import DictReader, DictWriter
with open('zalina.csv','r') as rf:
    with open('outputcsv.csv','w',newline="") as wf:
        csv_reader=DictReader(rf)
        # for i in csv_reader:
        #     print(i)
        csv_writer=DictWriter(wf,fieldnames=['FirstName','Nation'])   #header names
        csv_writer.writeheader()   #writing the header names

        for i in csv_reader:
            fname, nation= i['name'],i['country']    #assigning the values in variables

            csv_writer.writerow({    #Writing in new file,  writerow will take dictionary
                'FirstName':fname.upper(),      
                'Nation':nation.lower()
            })


















