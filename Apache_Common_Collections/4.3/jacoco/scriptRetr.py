import csv
'''reading excel'''
a=[]
with open('index.html', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		sp = row[1].split(".")
		if len(sp)==1:
			temp=[]
			temp.append(row[0])
			temp.append(row[1])
			temp.append(row[2])
			a.append(temp)
		
csvFile.close()
'''exporting to excel'''
with open('employee_file.csv', mode='w') as employee_file:
	employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for ro in a:
		employee_writer.writerow([ro[0], ro[1], ro[2]])
		