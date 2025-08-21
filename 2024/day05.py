#%%
f = 'data/day05.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('🐟 🎄 🦈')
#%%
page_rules = {}
updates = []

for l in read_lines:
    if '|' in l:
        x,y = map(int, l.split('|'))
        if x not in page_rules:
            page_rules[x] = [y]
        else:
            page_rules[x].append(y)
    elif ',' in l:
        pages = list(map(int, l.split(',')))
        updates.append(pages)
#%%
# verified all odd number of pages
# [len(x)%2 for x in updates]

mid_sum = 0
bad_rules = []
for pages in updates:
    fail = False
    for i, page in enumerate(pages):
        for page_rule in page_rules[page]:
            if page_rule in pages[:i]:
                fail = True
                break
        if fail:
            bad_rules.append(pages)
            break
    else:
        mid_sum += pages[len(pages)//2]
print(mid_sum)
#%%
def verify(pages):
    pages = pages[:]
    for i, page in enumerate(pages):
        for page_rule in page_rules[page]:
            if page_rule in pages[:i]:
                # swap page_rule and page
                pr_idx = pages.index(page_rule)
                pages[i] = page_rule
                pages[pr_idx] = page
                return True, pages
    return False, pages

mid_bad_sum = 0
for pages in bad_rules:
    bad_rule = True
    while bad_rule:
        bad_rule, pages = verify(pages)
    mid_bad_sum += pages[len(pages)//2]
print(mid_bad_sum)
#%%
