thing = {'pop': {2}, 'pop':{1}, 'pop':{3}}
new_thing = list(thing.get('pop', set()))
print(new_thing)