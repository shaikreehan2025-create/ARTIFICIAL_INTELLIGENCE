def map_coloring_csp():
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    colors = ['Red', 'Green', 'Blue']
    assignment = {}

    def is_safe(region, color):
        for neighbor in neighbors[region]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(idx=0):
        if idx == len(regions):
            return True
        region = regions[idx]
        for color in colors:
            if is_safe(region, color):
                assignment[region] = color
                if backtrack(idx + 1):
                    return True
                del assignment[region]
        return False

    print("Map Coloring Problem using CSP (Backtracking Search):")
    print(f"Regions (Variables): {regions}")
    print(f"Colors (Domain): {colors}\n")

    if backtrack():
        print("Consistent Map Coloring Solution Found:")
        for reg in regions:
            print(f"  {reg:4} -> {assignment[reg]}")
    else:
        print("No valid coloring exists.")

map_coloring_csp()