#%%
import regex as re

input = open('data/day7.txt')
read_lines = input.readlines()
# %%

bag_dict = {}

for l in read_lines:
    l = l.strip()
    if 'no other bags.' in l:
        re_result = re.search('(\D*) bags contain',l)
        groups = re_result.groups()
        bag_dict[groups[0]] = None
    else:
        re_result = re.search('(\D*) bags contain (?:(\d*) (\D*) bag[s, ]*)?(?:(\d*) (\D*) bag[s, ]*)?(?:(\d*) (\D*) bag[s, ]*)?(?:(\d*) (\D*) bag[s, ]*)?(?:(\d*) (\D*) bag[s, ]*)?(?:(\d*) (\D*) bag[s, ]*)?\.', l)
        groups = re_result.groups()
        for i, g in enumerate(groups[1:]):
            if g is not None and g in '123456789':
                if groups[0] in bag_dict:
                    bag_dict[groups[0]][groups[i+2]] = groups[i+1]
            
                else: 
                    bag_dict[groups[0]] = {groups[i+2]:groups[i+1]}
# %%
#! Part 1
shiny_gold_bag_holders = 0

def bag_searcher(bag_dict, key, shiny_gold):
    # print(f'key: {key} bags: {bag_dict[key]}, gold: {shiny_gold}')
    keys = bag_dict[key]
    if keys is None:
        return shiny_gold
    if 'shiny gold' in keys:
        shiny_gold += 1
        return shiny_gold
    for k in keys:
        shiny_gold = bag_searcher(bag_dict, k, shiny_gold)
    return shiny_gold

for bag in bag_dict.keys():
    shiny_gold = 0
    if bag_dict[bag] is not None:
        shiny_gold = bag_searcher(bag_dict, bag, shiny_gold)
        if shiny_gold > 0:
            shiny_gold_bag_holders += 1
            # print('Gold strike! no.',shiny_gold_bag_holders)
print('Part 1:', shiny_gold_bag_holders)


# %%
#! Part 2

#* This was super tricky. Needed to draw it out. bags * (1 + bags_inside)
def last_bag(bag_dict, key):
    keys = bag_dict[key]
    if keys is None:
        # print('end of the line', key)
        inner_bag_count = 0 #? bag count is zero for no more bags inside
        return inner_bag_count
    bag_count = 0
    for k in keys:
        inner_bag_count_k = int(bag_dict[key][k]) * (1 + last_bag(bag_dict, k))
        bag_count += inner_bag_count_k
    return bag_count

bags_in_bags = last_bag(bag_dict,'shiny gold')
print('Part 2:', bags_in_bags)

# %%
