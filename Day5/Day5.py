def parse_almanac(file_path):
    with open(file_path, 'r') as file:
        content = file.read().splitlines()

    # Initialize variables to store data
    seeds = []
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    current_map = None  # Track the current map being processed

    for line in content:
        # Check for category headers
        if line.startswith("seeds:"):
            seeds = list(map(int, line.split(":")[1].strip().split()))
        elif line.startswith("seed-to-soil map:"):
            current_map = seed_to_soil_map
        elif line.startswith("soil-to-fertilizer map:"):
            current_map = soil_to_fertilizer_map
        elif line.startswith("fertilizer-to-water map:"):
            current_map = fertilizer_to_water_map
        elif line.startswith("water-to-light map:"):
            current_map = water_to_light_map
        elif line.startswith("light-to-temperature map:"):
            current_map = light_to_temperature_map
        elif line.startswith("temperature-to-humidity map:"):
            current_map = temperature_to_humidity_map
        elif line.startswith("humidity-to-location map:"):
            current_map = humidity_to_location_map
        else:
            # Process the map lines
            if current_map is not None:
                mapping = list(map(int, line.split()))
                current_map.append(mapping)

    return {
        "seeds": seeds,
        "seed_to_soil_map": seed_to_soil_map,
        "soil_to_fertilizer_map": soil_to_fertilizer_map,
        "fertilizer_to_water_map": fertilizer_to_water_map,
        "water_to_light_map": water_to_light_map,
        "light_to_temperature_map": light_to_temperature_map,
        "temperature_to_humidity_map": temperature_to_humidity_map,
        "humidity_to_location_map": humidity_to_location_map
    }

def convert_number(seed, category_maps, current_category="seed_to_soil_map"):
    # if current_category =="seed_to_soil_map":
    #     print("Seed: ", seed)

    categories = list(category_maps.keys())
    category_index = categories.index(current_category)

    # Remove empty lists
    category_maps[current_category] = [sublist for sublist in category_maps[current_category] if sublist]

    dest_seed = None
    # Iterate through the category maps
    for dest_start, src_start, length in category_maps[current_category]:
        # Check if the seed falls within the source range 
        if src_start <= seed <= src_start + length - 1:
            # Check the position of the value in the list
            position = seed - src_start
            dest_seed = dest_start + position

    if dest_seed == None:
        dest_seed = seed

    # print(f"{current_category}: {dest_seed}")
    if current_category == 'humidity_to_location_map':
        # print("\n")    
        return dest_seed
    
    return convert_number(dest_seed, category_maps, current_category=categories[category_index+1])
        
# Example usage
file_path = 'input.txt'
almanac_data = parse_almanac(file_path)

# Find the lowest location number that corresponds to any of the initial seed numbers
lowest_location = [convert_number(seed, almanac_data) for seed in almanac_data["seeds"]]

print(f"Solution Part I: {min(lowest_location)}")

# Part II

# lowest_location = []
# for i in range(0, len(almanac_data["seeds"])-1, 2):
#     ini_value = almanac_data["seeds"][i]
#     end_value = almanac_data["seeds"][i+1]
#     new_seeds_list = (range(ini_value, ini_value+end_value-1))
#     lowest_location.append(min(convert_number(seed, almanac_data) for seed in new_seeds_list))

# print(f"Solution Part II: {min(lowest_location)}")

from collections import defaultdict
with open(file_path, 'r') as file:
   D = file.read().strip()

L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

def f(R, o):
  A = []
  for line in o:
    dest,src,sz = [int(x) for x in line.split()]
    src_end = src+sz

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print(min(P2))