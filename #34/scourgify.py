import sys
import csv
import tabulate

print(sys.argv)

#check command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith('.csv') and not sys.argv[2].endswith('.csv'):
    sys.exit("Not a CSV file")
elif FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


with open(sys.argv[1], 'r', newline='') as before:
    reader_before = csv.DictReader(before)
    all_rows = []
    for row in reader_before:
        first_name = row[1]
        last_name = row[0]
        house = row[2]
        all_rows.append({'first_name' : first_name, 'last_name' : last_name, 'house' : house})
    
    

with open(sys.argv[2], 'w', newline='') as after:
    writer_after = csv.DictWriter(after, fieldnames=['first_name', 'last_name', 'house'])
    writer_after.writeheader()
    writer_after.writerow(all_rows)
    # after.flush()

print(tabulate(writer_after))
