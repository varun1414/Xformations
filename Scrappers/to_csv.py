import csv
def convert(data,name):
        csv_columns = ['comp','date','result','teams','score','formation']
        dict_data = data
        csv_file = name
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
