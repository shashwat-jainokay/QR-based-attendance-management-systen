from prettytable import PrettyTable

csv_file = open('C:/Users/shash/Desktop/OOSE/Project/barcodes.csv','r')
csv_file=csv_file.readlines()
#with open(fname) as f:
for i, l in enumerate(csv_file):
    pass
line=[]
for x in range(0,i+1):
    
    line.append(csv_file[x])
    line[x]=line[x].split(',') 

table=PrettyTable(["Time","Name","Roll No.","Branch"])
for x in range(1,i+1):
    table.add_row(line[x])
html_code =table.get_html_string()
html_file = open('C:/Users/shash/Desktop/OOSE/Project/templates/Report.html','w')
html_file = html_file.write(html_code)   
