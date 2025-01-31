import csv

def get_file_names():
  # filenames = [tagged_tickets_0.csv, tagged_tickets_10.csv, ... tagged_tickets_970.csv]
  filenames = []
  for i in range(0, 80, 10):
    filenames.append(f'tagged_tickets_{i}.csv')
  return filenames

def read_file_get_rows(file_name):
  rows = []
  with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      rows.append(row)
  rows_without_header = rows[1:]
  return rows_without_header

def main():
  file_names = get_file_names()
  rows = []
  for file_name in file_names:
    rows.extend(read_file_get_rows(file_name))
  header = ['ticket_id','booking_id','description','IsTechnicalIssue','TechnicalIssue', 'isSpaceIssue', 'Amenity', 'SpaceExperience', 'Location', 'ConfusingUserJourney', 'ConfusingFeature', 'TechInterventionNeeded', 'ProductInterventionNeeded']
  rows.insert(0, header)
  with open('combined_tickets.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
  print('Combined tickets saved to combined_tickets.csv')

if __name__ == '__main__':
  main()