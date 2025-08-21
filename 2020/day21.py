#%%
f = 'data/day21.txt'
# f = 'data/day21ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
ingredient_counts = {}
allergens = {}
for line in read_lines:
    i,a = line.split(' (contains ')
    i = i.split(' ')
    a = a.strip(')')
    a = a.split(', ')
    
    for ing in i:
        if ing not in ingredient_counts:
            ingredient_counts[ing] = 0
        ingredient_counts[ing] += 1
    
    for al in a:
        if al not in allergens:
            allergens[al] = set()
        if allergens[al] == set():
            for ing in i:
                allergens[al].add(ing)
        else:
            safe_ingredients = []
            for al_ing in allergens[al]:
                if al_ing not in i:
                    safe_ingredients.append(al_ing)
            for al_ing in safe_ingredients:
                allergens[al].remove(al_ing)

safe_ingredients = [ing for ing in ingredient_counts if ing not in [a for al in allergens.values() for a in al]]
safe_ingredients_sum = sum([ingredient_counts[ing] for ing in safe_ingredients])
print(safe_ingredients_sum)
#%%
solved_allergens = {al:None for al in allergens}
while None in solved_allergens.values():
    for al, ing in allergens.items():
        if len(ing) == 1:
            [solved_ing] = ing
            solved_allergens[al] = solved_ing
    
    for s_a, s_i in solved_allergens.items():
        for al, ing in allergens.items():
            if s_a != al:
                if s_i in ing:
                    allergens[al].remove(s_i)
print(','.join(dict(sorted(solved_allergens.items())).values()))
#%%
