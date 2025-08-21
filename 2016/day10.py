#%%
import re

f = 'data/day10.txt'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
print('🎅 🎄 🤶')
#%%


class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.chips = []

    def id(self):
        print(f'Bot ID: {self.bot_id}')
        print(f'Chips: {self.bot_chips()}')
        print(f'Low: {self.low_go()}')
        print(f'High: {self.high_go()}')

    def set_low(self, low, low_type):
        self.low = low
        self.low_type = low_type

    def low_go(self):
        return self.low, self.low_type

    def set_high(self, high, high_type):
        self.high = high
        self.high_type = high_type

    def high_go(self):
        return self.high, self.high_type

    def bot_chips(self):
        return self.chips

    def add_chip(self, chip):
        self.chips.append(chip)
        self.sort_chips()

    def remove_chip(self, chip):
        self.chips.remove(chip)
        self.sort_chips()

    def sort_chips(self):
        self.chips.sort()

    def low_chip(self):
        return self.chips[0]

    def high_chip(self):
        return self.chips[-1]

    def chip_overload(self):
        return len(self.chips) >= 2

    def the_chosen_bot(self):
        if self.low_chip() == 17 and self.high_chip() == 61:
            return True
        return False


# init the bots and outputs
bots = {}
outputs = {}
for line in read_lines:
    digits = re.findall(r'\d+', line)
    digits = map(int, digits)

    if 'value' in line:
        v, b = digits
        if b not in bots:
            bots[b] = Bot(b)
        bots[b].add_chip(v)

    else:
        a, b, c = digits
        bob, boc = [line.split()[i] for i in [5, 10]]
        if a not in bots:
            bots[a] = Bot(a)
        bots[a].set_low(b, bob)
        bots[a].set_high(c, boc)


# find initial overloaded bot
overloaded_bot = -1
for k, b in bots.items():
    if bots[k].chip_overload() is True:
        print(f'BOT OVERLOAD {k}')
        overloaded_bot = k

#%%
new_loaded_bots = [overloaded_bot]
loaded_bots = []
the_savior_bot = 'has not returned'
sacrifice = False
while ((the_savior_bot == 'has not returned') or (sacrifice is False)):
    if '😇' not in the_savior_bot:
        print(f'the savior bot {the_savior_bot}')
    else:
        print('the savior demands 🐇 †')
    loaded_bots = [_ for _ in new_loaded_bots if _ not in loaded_bots]  # prevents bot 198 from being selected 2x at the start and breaking everything.
    new_loaded_bots = []
    for b in loaded_bots:
        # print(f'bot {b} is processing')
        # bots[b].id()
        if bots[b].the_chosen_bot():
            the_savior_bot = 'has returned 😇!'
            print(f'the savior bot {the_savior_bot}')
            print(f'bot {b} is the chosen one!')

        #! part 2
        if the_savior_bot == 'has returned 😇!':
            if 0 in outputs and 1 in outputs and 2 in outputs:
                print(f'{outputs[0]*outputs[1]*outputs[2]} 🐇 †')
                sacrifice = True
                break

        if bots[b].chip_overload():
            low, low_type = bots[b].low_go()
            high, high_type = bots[b].high_go()

            if low_type == 'bot':
                bots[low].add_chip(bots[b].low_chip())
                new_loaded_bots.append(low)
            else:
                outputs[low] = bots[b].low_chip()
            bots[b].remove_chip(bots[b].low_chip())

            if high_type == 'bot':
                bots[high].add_chip(bots[b].high_chip())
                new_loaded_bots.append(high)
            else:
                outputs[high] = bots[b].high_chip()
            bots[b].remove_chip(bots[b].high_chip())


#%%
print()
print('⭐ ⭐')
