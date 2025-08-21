#%%
f = 'data/day13.txt'
# f = 'data/day13.ex'

with open(file=f) as input:
    patterns = input.read().strip().split('\n\n')
    patterns = [p.split('\n') for p in patterns]
print('❄️⛄❄️')


def mirror(pattern, part_2 = False):
    mirror_i = []
    R = len(pattern)
    for i, r_i in enumerate(pattern[:-1]):
        for j, r_j in enumerate(pattern[i+1:i+2],start=i+1):
            if r_i == r_j:
                # check for symmetry
                for m_i, m_j in zip(range(i-1,-1,-1),range(j+1,R,1)):
                    if pattern[m_i] != pattern[m_j]:
                        break
                else:
                    if part_2 is False:  # part 1 only 1 match
                        return i+1
                    mirror_i.append(i+1)
    return mirror_i


ans = 0
for pattern in patterns:
    m_p = mirror(pattern)
    if m_p != []:
        ans += 100 * m_p
    else:
        # transpose
        pattern_t = list(map(list, zip(*pattern)))
        m_p_t = mirror(pattern_t)
        ans += 1 * m_p_t
print('🪞:', ans)


#! part 2
def smuge_mirror(pattern):
    for i, r_i in enumerate(pattern[:-1]):
        for j, r_j in enumerate(pattern[i+1:],start=i+1):
            if (i + j) % 2 == 0:  # only check odd, boundary must be between lines
                continue
            smuges_required = sum([a != b for a,b in zip(r_i,r_j)])
            if smuges_required == 1:
                smuged_pattern = pattern[:]
                smuged_pattern[j] = r_i
                m_p_s = mirror(smuged_pattern, part_2=True)
                m_p = mirror(pattern, part_2=True)
                if m_p_s != []:
                    #! must be a different reflection
                    diff = set(m_p_s).difference(set(m_p))
                    if len(diff)>0:
                        return diff.pop()
    return []


ans = 0
for pattern in patterns:
    m_p = smuge_mirror(pattern)
    if m_p != []:
        ans += 100 * m_p
    else:
        pattern_t = list(map(list, zip(*pattern)))  # transpose
        m_p_t = smuge_mirror(pattern_t)
        ans += 1 * m_p_t
print('🪞:', ans)

#%%
