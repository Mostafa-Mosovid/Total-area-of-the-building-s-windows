import csv 
total_area = 0.0
with open('windows_dimensions.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        length = float(row['length'])
        width = float(row['width'])
        total_area += length * width
print(f"Total area of windows is: {total_area}")
