import hebi
from time import sleep
lookup = hebi.Lookup()
# Give the Lookup process 2 seconds to discover modules
sleep(2)
print('Modules found on network:')


families = ['digger', 'digger', 'digger', 'digger']
names = ['shoulder', 'elbow', 'wrist', 'base']

group = lookup.get_group_from_names(families, names)
group = lookup.get_group_from_family('*')

for entry in lookup.entrylist:
  print(f'{entry.family} | {entry.name}')
