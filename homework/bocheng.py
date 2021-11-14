def n_bishops(n, bishop_locs, target):

    def good_placement(assignment, newBishop):
        for bishop in assignment:
            if abs(bishop[0] - newBishop[0]) == abs(bishop[1] - newBishop[1]):
                return False
        return True

    def next_spaces(n, assignment):
        spaces = []
        for x in range(n):
            for y in range(n):
                if (x, y) not in assignment:
                    spaces.append((x, y))
        return spaces

    def place_bishop(n, bishop_locs, assignment, target):
        if len(assignment) == target:
            return True

        spaces = next_spaces(n, assignment)
        for newX, newY in spaces:
            if good_placement(assignment, (newX, newY)):
                assignment.add((newY, newY))
                if place_bishop(n, bishop_locs, assignment, target):
                    return True
                assignment.remove((newX, newY))
        return

    assignment = bishop_locs.copy()
    place_bishop(n, bishop_locs, assignment, target)
    if assignment == bishop_locs:
        return None
    return assignment


print(n_bishops(3, set(), 4))
