from sys import argv, exit
import csv

w

try:
    with open(argv[1]) as before:
        reader = csv.DictReader(before)
        with open(argv[2], 'w') as after:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(after, fieldnames=fieldnames)
            writer.writeheader()
            try:
                for line in reader:
                    last, first = line['name'].split(',')
                    writer.writerow({'first' : first.lstrip(), 'last' : last.lstrip(), 'house' : line['house']})
            except KeyError:
                exit('File is not readable')
except FileNotFoundError:
    exit('File not found')