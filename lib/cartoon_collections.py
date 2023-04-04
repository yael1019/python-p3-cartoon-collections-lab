def roll_call_dwarves(arr):
    for index, name in enumerate(arr):
        print(f'{index + 1}. {name}')

def summon_captain_planet(arr):
    return [f'{name.capitalize()}!' for name in arr]

def long_planeteer_calls(arr):
    for value in arr:
        print(len(value))
        if len(value) > 4:
            return True
    return False

def find_the_cheese(arr):
    if "cheddar" in arr:
        return "cheddar"
    elif "gouda" in arr:
        return "gouda"
    elif "camembert" in arr:
        return "camembert"
    else:
        return None
