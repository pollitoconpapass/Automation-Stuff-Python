import camelot 

tables = camelot.read_pdf('sample.pdf', pages='1')
print(tables)

# ---EXPORTING TO A CSV FILE ---
tables.export('sample.csv', f= 'csv', compress=True)
tables[0].to_csv('sample.csv') #-> export just the first table  