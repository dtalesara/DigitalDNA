def apply_epigenetics(raw_value, epigenetic_factors, weights):
    modifier = 0.0
    for key, value in epigenetic_factors.items():
        modifier += weights.get(key, 0.0) * value
    return raw_value + modifier
