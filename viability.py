MODULES = {
    "hab": {
        "volume": 50, "food_storage": 100, "water_storage": 200, "oxygen_storage": 20,
    },
    "solar": {
        "energy_generation": 120, # kWh/day
    },
    "greenhouse": {
        "food_generation": 2, # kg/day
        "oxygen_generation": 1, # kg/day
        "water_generation": 0.5, # L/day
    },
    "store": {
        "food_storage": 300, "water_storage": 500, "oxygen_storage": 40, "energy_storage": 1000,
    },
    "lab": {
        "volume": 30,
    },
    "medical": {
        "volume": 20,
        "oxygen_storage": 5,
    },
    "base": {
        "volume": 40,
    }
}

# Of people
DAILY_NEEDS = {
    "food": 0.8,       # kg per person per day
    "o2": 0.84,        # kg per person per day
    "water": 10.0,      # L per person per day
    "energy": 7,       # kWh per person per day
    "volume": 29,      # m³ per person (static, not daily)
}

def calculate_viability(modules, crew, days):
    avail = dict(food=0, o2=0, water=0, energy=0, volume=0)
    for m in modules:
        data = MODULES.get(m['type'], {})
        # Storage
        avail['food'] += data.get('food_storage', 0)
        avail['o2'] += data.get('oxygen_storage', 0)
        avail['water'] += data.get('water_storage', 0)
        avail['energy'] += data.get('energy_storage', 0)
        avail['volume'] += data.get('volume', 0)
        # Generation per day
        avail['food'] += days * data.get('food_generation', 0)
        avail['o2'] += days * data.get('oxygen_generation', 0)
        avail['water'] += days * data.get('water_generation', 0)
        avail['energy'] += days * data.get('energy_generation', 0)
    # Needs
    needs = {
        'food': crew * days * DAILY_NEEDS['food'],
        'o2': crew * days * DAILY_NEEDS['o2'],
        'water': crew * days * DAILY_NEEDS['water'],
        'energy': crew * days * DAILY_NEEDS['energy'],
        'volume': crew * DAILY_NEEDS['volume'],
    }
    subs = {k: min(avail[k]/needs[k], 1.0) if needs[k]>0 else 1.0 for k in avail}
    VI = sum(subs.values()) / len(subs)
    return {'subindexes': subs, 'VI': VI, 'needs': needs, 'available': avail}
