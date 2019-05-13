#! /usr/local/bin/python3

def evaluate_actions(actions):
    # action is list of string, each of string denotes the an action
    location_map = {}
    status_map = {}
    strength_map = {}

    # populate location map
    for action in actions:
        params = action.split(" ")
        army, ac = params[0], params[2]
        new_location = ""
        if ac == "Hold" or ac == "Support":
            new_location = params[1]
        else:
            new_location = params[3]
        if new_location not in location_map:
            location_map[new_location] = []
        location_map[new_location].append(army)
    print("check location_map: %s" %repr(location_map))

    # populate strength map
    for action in actions:
        params = action.split(" ")
        army, ac = params[0], params[2]
        if army not in strength_map:
            # initialize each army with strength of 0
            strength_map[army] = 0
        if ac == "Support":
            support_location = params[1]
            supportee = params[3]
            # if only 1 army in support_location, support validated
            if len(location_map[support_location]) == 1:
                supportee_strength = strength_map.get(supportee, 0) + 1
                strength_map[supportee] = supportee_strength
    print("check strength_map: %s" %repr(strength_map))

    for key, val in location_map.items():
        location = key
        army_list = val
        if len(army_list) == 1:
            status_map[army_list[0]] = location
            continue
        # start from first army, take it as winner -- army of max strength
        max_army = army_list[0]
        max_strength = strength_map[max_army]
        for i in range(1, len(army_list)):
            army = army_list[i]
            strength = strength_map[army]
            if strength < max_strength:
                status_map[army] = "[dead]"
                status_map[max_army] = location
            elif strength == max_strength:
                status_map[army] = "[dead]"
                status_map[max_army] = "[dead]"
            else:
                status_map[max_army] = "[dead]"
                max_army = army
                max_strength = strength
                status_map[max_army] = location
    print("check status_map: %s" %repr(status_map))

    res = []
    for key, val in status_map.items():
        item = key + " " + val
        res.append(item)
    res.sort()
    return res

test_cases = [
    [
        "A Munich Hold",
        "B Warsaw Move Bohemia"
    ],
    [
        "A Munich Hold",
        "B Bohemia Move Munich",
        "C Warsaw Support B"
    ],
    [
        "A Munich Hold",
        "B Bohemia Move Munich",
        "C Prussia Move Munich",
        "D Warsaw Hold"
    ],
    [
        "A Munich Support B",
        "B Bohemia Move Prussia",
        "C Prussia Hold",
        "D Warsaw Move Munich"
    ],
    [
        "A Munich Support B",
        "B Oakland Move Munich"
    ],

    [
        "A Munich Hold",
        "B Warsaw Move Bohemia",
    ],
    [
        "A Munich Hold",
        "B Bohemia Move Munich",
        "C Warsaw Support B"
    ],
    [
        "A Munich Hold",
        "B Bohemia Move Munich",
        "C Prussia Move Munich",
        "D Warsaw Hold"
    ],
    [
        "A Munich Support B",
        "B Bohemia Move Prussia",
        "C Prussia Hold",
        "D Warsaw Move Munich"
    ],
    [
        "A Munich Support B",
        "B Oakland Move Munich"
    ],
    []
]
for test_input in test_cases:
    print("input: %s" %test_input)
    res = evaluate_actions(test_input)
    print(res)
