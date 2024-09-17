import csv

def main():

    customers = open('customers.csv', 'r')
    
    customer_country = open('customer_country.csv', 'w', newline='')
        
    reader = csv.reader(customers)
    writer = csv.writer(customer_country)
        
    writer.writerow(["Full Name", "Country"])
       
    next(reader)
        
    for row in reader:
            writer.writerow([f"{row[1]} {row[2]}", row[4]])
    
    customer_country.close()

main()



