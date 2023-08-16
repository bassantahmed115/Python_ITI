from myexperianepackage.simplefile.file_operations import read_file, write_file, read_excel, write_excel
import pandas as pd

# Test the file operations
file_content = read_file('test.txt', 'r')
print("File Content:")
print(file_content)

write_file('output.txt', file_content)
print("File written successfully.")

# Test the Excel operations
excel_data = [
    ['Name', 'Age'],
    ['Alice', 28],
    ['Bob', 35],
]

write_excel('data.xlsx', excel_data)
print("Excel file written successfully.")

read_data = read_excel('data.xlsx', 'Sheet')
print("Excel Data:")
print(read_data)
