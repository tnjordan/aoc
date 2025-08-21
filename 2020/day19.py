#%%
f = 'data/day19.txt'
# f = 'data/day19ex.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [line.strip() for line in read_lines]
print('❄️⛄❄️')
#%%
rules = {}
messages = []

for line in read_lines:
    if ':' in line:
        rule, pattern = line.split(': ')
        
        pattern_parts = pattern.split('|')
        pattern = []
        for p_p in pattern_parts:
            pattern.append(p_p.strip().split())
        
        rules[rule] = pattern
    elif line == '':
        continue
    else:
        messages.append(line)
#%%
part_2 = True
if part_2:
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]

solved_rules = {
    'a': ['a'],
    'b': ['b']
}

def solve_rule(rule):
    pattern = rules[rule]
    solved_patterns = []
    
    for pat in pattern:
        alternatives = ['']
        for p in pat:
            new_alternatives = []
            expansions = solved_rules[p]
            for alt in alternatives:
                for exp in expansions:
                    new_alternatives.append(alt + exp)
            alternatives = new_alternatives
        solved_patterns.extend(alternatives)
    solved_rules[rule] = solved_patterns

#! GPT solution with print statements to step through process
# def solve_rule(rule):
#     print(f"\n=== Solving rule {rule} ===")
#     pattern = rules[rule]
#     print(f"Pattern for rule {rule}: {pattern}")
#     solved_patterns = []
    
#     for i, pat in enumerate(pattern):
#         print(f"\n  Alternative pattern #{i+1}: {pat}")
#         # For each alternative pattern
#         alternatives = ['']
#         print(f"  Starting alternatives: {alternatives}")
        
#         # Process each symbol in the pattern
#         for j, p in enumerate(pat):
#             print(f"\n    Processing symbol {j+1}: '{p}'")
#             new_alternatives = []
            
#             # Get all possible expansions for this symbol
#             expansions = solved_rules[p]
#             print(f"    Expansions for '{p}': {expansions}")
            
#             # Combine each existing alternative with each expansion
#             print(f"    Current alternatives: {alternatives}")
#             print(f"    Combining each alternative with each expansion:")
            
#             for alt in alternatives:
#                 for exp in expansions:
#                     combined = alt + exp
#                     new_alternatives.append(combined)
#                     print(f"      '{alt}' + '{exp}' = '{combined}'")
            
#             alternatives = new_alternatives
#             print(f"    Updated alternatives: {alternatives}")
        
#         print(f"\n  Final alternatives for pattern #{i+1}: {alternatives}")
#         solved_patterns.extend(alternatives)
    
#     print(f"\nSolved patterns for rule {rule}: {solved_patterns}")
#     solved_rules[rule] = solved_patterns
#     print(f"Added rule {rule} to solved_rules\n")
#     return solved_patterns

def find_solved_rules(rules):
    for rule, pattern in rules.items():
        if rule in solved_rules: 
            continue
        
        pattern_values = set(value for sublist in pattern for value in sublist)
        # Check if all values are keys in solved_rules
        all_in_solved_rules = all(value in solved_rules.keys() for value in pattern_values)
        
        if all_in_solved_rules:
            solve_rule(rule)
#%%
if not part_2:
    while '0' not in solved_rules:
        find_solved_rules(rules)
    valid_messages = 0
    for m in messages:
        if m in solved_rules['0']:
            valid_messages += 1
    print(f'valid messages: {valid_messages}')
else:
    while '31' not in solved_rules or '42' not in solved_rules:
        find_solved_rules(rules)
    valid_messages = 0
    for message in messages:
        the_answer = True
        valid_42_segments = 0
        valid_31_segments = 0
        for i in range(0,len(message), 8):  # both 42 and 31 had only len 8 messages
            message_segment = message[i:i+8]
            if the_answer:
                if message_segment in solved_rules['42']:
                    valid_42_segments += 1
                    continue
                else:
                    the_answer = False
            if not the_answer:
                if message_segment in solved_rules['31']:
                    valid_31_segments += 1
                    continue
                else:
                    break
        else:
            if valid_42_segments > 0 and valid_31_segments > 0 and valid_42_segments > valid_31_segments:
                valid_messages += 1
    print(f'valid messages: {valid_messages}')
#%%
