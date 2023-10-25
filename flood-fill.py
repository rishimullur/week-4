#Problem to solve the flood-fill problem
def flood_fill(input_board, old, new, x, y):
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str]): The input board
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    #Add ASSERT for both row & column numbers
        

    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
	return input_board

    # Check if the current cell contains the old value
    if input_board[x][y] == old:
        # Replace the old value with the new value
	# logic for "....x..." replace x with new
        input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]

	#Do a recursion function call
	flood_fill(input_board, old, new, x + 1, y)
        flood_fill(input_board, old, new, x - 1, y)
        flood_fill(input_board, old, new, x, y + 1)
        flood_fill(input_board, old, new, x, y - 1)

    return input_board

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

new_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

# Print the modified board
for row in new_board:
    print(row)
