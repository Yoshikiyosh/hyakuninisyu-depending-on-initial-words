import csv
csv_file_path = '100poets.csv'
sentences = []
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        sentence = row[1] 
        sentences.append(sentence)


def get_animals( animals, n ):
  prefixes = [ animal[0:n] for animal in animals] 
  unique_prefixes = tuple( c for c in set( prefixes ) if prefixes.count(c)==1 )
  return [ p for p in animals if p.startswith(unique_prefixes) ]
animals = set( sentences )
n = 1
while animals: 
  selected = get_animals( animals, n )
  print('■', n, "字きまり")
  for animal in sorted(selected): 
    print({ animal } )
  animals -= set(selected) 
  n += 1
