#%%
from collections import Counter

f = open('data\day19_input.txt', 'r')
read_lines = f.readlines()
f.close()

scanner = []
count = 0
for l in read_lines:
    count += 1
    l = l.strip()
    if 'scanner' in l:
        s = []
    elif ',' in l:
        x,y,z = l.split(',')
        s.append([int(x),int(y),int(z)])
    else:
        scanner.append(s)

#direction changer #TODO fix this it is poor form
L = [0,1,2]
coord_change = []
for i in L:
    for j in L:
        if j != i:
            for k in L:
                if k != i and k != j:
                    coord_change.append([i,j,k])

def beacon_map(scan,i):
    dist_map_dict = {}
    for s1 in scan:
        for s2 in scan:
            if s1 != s2:
                delta_x = abs(s1[0] - s2[0])
                delta_y = abs(s1[1] - s2[1])
                delta_z = abs(s1[2] - s2[2])
                if (delta_x, delta_y, delta_z) not in dist_map_dict.keys():
                    dist_map_dict[(delta_x, delta_y, delta_z)] = [[i,s1,s2]]
                else:
                    dist_map_dict[(delta_x, delta_y, delta_z)].append([i,s1,s2])
    return dist_map_dict

def beacon_matcher(b_positions, b_positions_dict, scan, bc, scanner_positions):
    matches = []
    match_points = {}
    overlap_count = 0
    for i,j,k in coord_change:
        for delta_1, delta_2, delta_3 in bc.keys():
            delta_L = [delta_1, delta_2, delta_3]
            if (delta_L[i],delta_L[j],delta_L[k]) in b_positions_dict.keys():
                overlap_count += 1
                matches.append([(delta_L[i], delta_L[j], delta_L[k]),(delta_1, delta_2, delta_3)])
                #* make dictionary of match points
                #* points in stable ref frame
                L_0 = b_positions_dict[(delta_L[i], delta_L[j], delta_L[k])][0][1]
                L_1 = b_positions_dict[(delta_L[i], delta_L[j], delta_L[k])][0][2]
                #* positions in rotated frame
                L_r0 = bc[(delta_1, delta_2, delta_3)][0][1]
                L_r1 = bc[(delta_1, delta_2, delta_3)][0][2]
                #* positions in same frame (some directions might be flipped)
                x_p0 = L_r0[i]
                y_p0 = L_r0[j]
                z_p0 = L_r0[k]
                x_p1 = L_r1[i]
                y_p1 = L_r1[j]
                z_p1 = L_r1[k]
                #* need to matchup the points
                for L in [L_0,L_1]: #* go through both points in the stable ref frame
                    if (L[0],L[1],L[2]) not in match_points.keys():
                        #* if we don't have a dictionary add the two possible points
                        match_points[(L[0],L[1],L[2])] = [(x_p0, y_p0, z_p0),(x_p1, y_p1, z_p1)]
                    else:
                        #* add points to the dictionary
                        match_points[(L[0],L[1],L[2])].append((x_p0, y_p0, z_p0))
                        match_points[(L[0],L[1],L[2])].append((x_p1, y_p1, z_p1))
                        
            if overlap_count > 12:
                #* solve for matching points (only 3 needed for triangulation but have more do too problem constraints)
                point_pairs = {}
                for key,v in match_points.items():
                    if len(v) > 2:
                        counts = Counter(v)
                        max_v = max(counts.values())
                        dict_pos = list(counts.values()).index(max_v)
                        point_match = list(counts.keys())[dict_pos]
                        match_points[key] = point_match
                for key,v in match_points.items():
                        if type(v) is tuple:
                            point_pairs[key] = v
                while len(point_pairs) < len(match_points):
                    for key,v in match_points.items():
                        if type(v) is list:
                            if v[0] in point_pairs.values():
                                point_pairs[key] = v[1]
                                match_points[key] = v[1]
                            elif v[1] in point_pairs.values():
                                point_pairs[key] = v[0]
                                match_points[key] = v[0]
                #flip values are either 1 or -1
                flip_x = -1
                flip_y = -1
                flip_z = -1
                #* adjust for axis flipping
                dx = None
                dy = None
                dz = None
                for key,v in point_pairs.items():
                    #* on first run all flips
                    if dx != key[0] + flip_x*v[0]:
                        flip_x *= -1
                    if dy != key[1] + flip_y*v[1]:
                        flip_y *= -1
                    if dz != key[2] + flip_z*v[2]:
                        flip_z *= -1
                    dx = key[0] + flip_x*v[0]
                    dy = key[1] + flip_y*v[1]
                    dz = key[2] + flip_z*v[2]
                
                #for key,v in point_pairs.items():
                #    print('good',key,'bad',v, 'shifted bad', (-flip_x*v[0] + dx, -flip_y*v[1] + dy ,-flip_z*v[2] + dz))
                #    print('shifted == key? ', (-flip_x*v[0] + dx, -flip_y*v[1] + dy ,-flip_z*v[2] + dz) == key)
                new_scan = []
                for s in scan:
                    #print()
                    #print('scan reading',tuple(s),'x,y,z ijk shuffled',(s[i],s[j],s[k]), 'i,j,k',i,j,k, 'modified', (-flip_x*s[i] + dx, -flip_y*s[j] + dy ,-flip_z*s[k] + dz))
                    #print('pos in b_pos ',[-flip_x*s[i] + dx, -flip_y*s[j] + dy ,-flip_z*s[k] + dz] in b_positions)
                    new_scan.append([-flip_x*s[i] + dx, -flip_y*s[j] + dy ,-flip_z*s[k] + dz])
                new_bc = beacon_map(new_scan,0)
                scanner_positions.append((dx,dy,dz))
                b_positions = b_positions + new_scan
                b_positions_dict.update(new_bc)
                return b_positions, b_positions_dict, True, scanner_positions
        overlap_count = 0
    return b_positions, b_positions_dict, False, scanner_positions

#def match_combine():

#* set initial positions based on scanner 0
b_positions = scanner[0]
b_positions_dict = beacon_map(scanner[0],0)
scanner = scanner[1:]

scanner_positions = [(0,0,0)]
while len(scanner) > 0:
    print('LETS GO')
    for i,scan in enumerate(scanner):
        bc = beacon_map(scan,i+1)
        b_positions, b_positions_dict, update_status, scanner_positions = beacon_matcher(b_positions, b_positions_dict, scan, bc, scanner_positions)
        if update_status is True:
            print('pop')
            scanner.remove(scan)

b_positions_set = []
for b in b_positions:
    b_positions_set.append(tuple(b))
b_positions_set = set(tuple(b_positions_set))

answer = len(b_positions_set)
print("ANSWER!", answer)

#%%

#! PART 2
max_manhattan = 0
for pos1 in scanner_positions:
    print(pos1)
    for pos2 in scanner_positions:
        #print(pos2)
        man_d = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) + abs(pos1[2]-pos2[2])
        if man_d > max_manhattan:
            max_manhattan = man_d
            print(max_manhattan)

print('Maximum Manhattan distance between scanners:',max_manhattan)
