# Colors

# Constrain values to fit within a boundary
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


# Wrap values if they go over a boundary
def wrap(val, min_val, max_val):
    if val > max_val:
        val = min_val
    if val < min_val:
        val = max_val
    return val