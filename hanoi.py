import random as rd

n_rings     = 5
n_towers    = 3
range_min   = 0
range_max   = 20

def rand_percentage(_min, _max)   : return rd.randint(_min, _max)

def rand_num(): 
    return rd.randint(range_min, range_max)

def generate_rings(n_rings):
    return [rand_num() for _ in range(n_rings)]

def generate_towers(): 
    return [generate_rings(n_rings) for _ in range(n_towers)]

hanoi = generate_towers()

def display (): 
    for tower in hanoi:
        print(tower)

# 1/ check the smallest top most ring as x 
# 2/ check if lower > x then place it in an array then repeat 2 else check
# if x < somewhere then append x into that tower else skip

display()
# Have current as smallest
# compare the towers where is the smallest aside from current
