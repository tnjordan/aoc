#%%
import re
import copy
from typing import Literal

f = 'data/day11.txt'
f = 'data/day11.ex'

with open(file=f) as input:
    read_lines = input.readlines()
read_lines = [li.strip() for li in read_lines]
#print('🎅 🎄 🤶')
#%%


class Floor:
    def __init__(self, id, generators, microchips):
        self.id = id
        self.generators = generators
        self.microchips = microchips

    def status(self):
        #print(f'\nid: \t\t\t{self.id}')
        #print(f'generators: \t{self.generators}')
        #print(f'microchips: \t{self.microchips}')
        pass

    def load(self, element, type):
        if type == 'generator':
            self.generators.append(element)
        elif type == 'microchip':
            self.microchips.append(element)

    def unload(self, element, type):
        if type == 'generator':
            self.generators.remove(element)
        elif type == 'microchip':
            self.microchips.remove(element)
    
    def do_nothing(self, elemet, type):
        pass

    def item_count(self):
        return len(self.generators) + len(self.microchips)


class Elevator(Floor):
    def __init__(self, id, generators, microchips, current_floor):
        super().__init__(id, generators, microchips)
        self.current_floor = current_floor

    def status(self):
        super().status()
        #print(f'current floor: \t{self.current_floor}')

    def load(self, element, type):
        #print(f'loading {type} {element}')
        if self.item_count() <= 1:
            super().load(element, type)
            # floors[self.current_floor].unload(element, type)  # only works in single run now recursive
            return True
        else:
            #print('Elevator Full!')
            return False

    def unload(self, element, type):
        #print(f'unloading {type} {element}')
        super().unload(element, type)
        # floors[self.current_floor].load(element, type)
        return True

    def elevate(self, direction: Literal[1, 0, -1]):
        #print(f'elevator requesting to move from {self.current_floor} {direction} floor to {self.current_floor + direction}')
        if self.current_floor + direction not in floors:
            #print('Invalid Floor!')
            return False
        if self.item_count() >= 1:
            self.current_floor += direction
            return True
        else:
            #print('Elevator Empty!')
            return False

    def generators_on_floor(self, floors):
        return self.generators + floors[self.current_floor].generators

    def microchips_on_floor(self, floors):
        return self.microchips + floors[self.current_floor].microchips

    def chip_fry(self, floors):
        generators_on_floor = self.generators_on_floor(floors)
        microchips_on_floor = self.microchips_on_floor(floors)
        if not generators_on_floor:
            return False
        fried_chips = set(microchips_on_floor) - set(generators_on_floor)
        if fried_chips:
            #print(f'microchips: {fried_chips} fried')
            return True
        else:
            return False

    def solved(self, floors):
        items = 0
        for fl in [1, 2, 3]:
            items += floors[fl].item_count()
        if items == 0:
            return True
        return False


generator_locator = re.compile(r'(\w*) generator')
microchip_locator = re.compile(r'(\w*)-compatible microchip')

floors = {}
floors['e'] = Elevator('e', [], [], 1)
for floor, line in enumerate(read_lines, start=1):
    # #print(f'floor {floor}')
    generators = re.findall(generator_locator, line)
    microchips = re.findall(microchip_locator, line)
    # #print(f'generators: {generators}')
    # #print(f'microchips: {microchips}')
    floors[floor] = Floor(id=floor, generators=generators, microchips=microchips)


def status(floors):
    for fl in floors:
        floors[fl].status()


status(floors)
#%%
global min_steps
min_steps = 12


def solve(steps, floors):
    #print(f'👣 steps: {steps} 👣')
    status(floors)
    global min_steps
    elevator = floors['e']
    if elevator.chip_fry(floors):
        return False
    if steps >= min_steps:
        return False
    if elevator.solved(floors):
        print(f'SOLVED!'*100)
        if min_steps < steps:
            min_steps = steps
    generators_on_floor = elevator.generators_on_floor(floors)
    generators_on_floor = [(g, 'generator') for g in generators_on_floor]
    microchips_on_floor = elevator.microchips_on_floor(floors)
    microchips_on_floor = [(m, 'microchip') for m in microchips_on_floor]
    steps += 1
    #print(f'🐛 Elevator is on floor: {elevator.current_floor}')
    for element, type in generators_on_floor + microchips_on_floor:
        #print(f'generators_on_floor + microchips_on_floor: {generators_on_floor + microchips_on_floor}')
        #print(f'on {type} {element}')
        new_floors = copy.deepcopy(floors)
        #print('🐞')
        status(new_floors)
        elevator = new_floors['e']
        if type == 'generator':
            if element in elevator.generators:
                for option in ['unload', 'do_nothing']:
                    if option != 'do_nothing':
                        load_status = elevator.unload(element, type)
                        if load_status:
                            new_floors[elevator.current_floor].load(element, type)
                    else:
                        load_status = True
            else:
                for option in ['load', 'do_nothing']:
                    if option != 'do_nothing':
                        load_status = elevator.load(element, type)
                        if load_status:
                            new_floors[elevator.current_floor].unload(element, type)
                    else:
                        load_status = True

        elif type == 'microchip':
            if element in elevator.microchips:
                for option in ['unload', 'do_nothing']:
                    if option != 'do_nothing':
                        load_status = elevator.unload(element, type)
                        if load_status:
                            new_floors[elevator.current_floor].load(element, type)
                    else:
                        load_status = True
            else:
                for option in ['load', 'do_nothing']:
                    if option != 'do_nothing':
                        load_status = elevator.load(element, type)
                        if load_status:
                            new_floors[elevator.current_floor].unload(element, type)
                    else:
                        load_status = True

        if load_status:
            for direction in [1, -1, 0]:
                new_new_floors = copy.deepcopy(new_floors)
                elevator = new_new_floors['e']
                elevate_status = elevator.elevate(direction)
                if elevate_status:
                    solve(steps, new_new_floors)


solve(0, floors)


#%%
# #print()
# #print('⭐ ⭐')
