"""
S125 HIT137 SOFTWARE NOW
Group Assignment 2 - Part 3
Group - CAS/DAN 10

"""

import turtle

# Draw tree using given data
def draw_tree(t, length, angle_left, angle_right, depth, scale, is_branch=False):
    
    """
    Parameters:
        t (turtle.Turtle): The turtle used to draw each branch.
        length (float): Length of the current branch being drawn.
        angle_left (float): Angle to turn for drawing the left branch.
        angle_right (float): Angle to turn for drawing the right branch.
        depth (int): How many levels of branching to draw (controls recursion depth).
        scale (float): Factor by which each branch shrinks compared to its parent.
        is_branch (bool): Indicates whether the current segment is a branch (True) 
                          or part of the trunk/main stem (False). Can be used to change 
                          appearance, like color.
    """

    if depth == 0:
        return

    # Set branch color
    if is_branch == True:
        t.pencolor("green")
        t.pensize(1)
    else:
        t.pencolor("brown")
        t.pensize(2)

    t.pendown()
    t.forward(length)

    # Save current state
    current_position = t.pos()
    current_heading = t.heading()

    # For left branch drawing
    t.left(angle_left)
    draw_tree(t, length * scale, angle_left, angle_right, depth - 1, scale, True)

    # For right branch drawing
    t.setpos(current_position)
    t.setheading(current_heading)
    t.right(angle_right)
    draw_tree(t, length * scale, angle_left, angle_right, depth - 1, scale, True)

    # Restore again turtle position
    t.setpos(current_position)
    t.setheading(current_heading)
    t.backward(length)

    t.penup()

# Initializes turtle
def initializing_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed("fastest")
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.pensize(2)
    return t

def main():
    print(f"*** Tree Pattern Generator Generator ***")

    # Get user input and validate those
    try:
        angle_left = float(input("Left branch angle (degrees): "))
        angle_right = float(input("Right branch angle (degrees): "))
        start_length = float(input("Starting branch length (pixels): "))
        depth = int(input("Recursion depth: "))
        reduction_factor = int(input("Branch length reduction factor (0 - 10): "))

        reduction_factor = reduction_factor / 10

    except ValueError:
        print(f"Invalid input. Please enter numbers only.")
        return
    
    if depth == 0:
        print(f"No more branches to draw.")
        exit()

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Tree Pattern Generator")

    turtle_instance = initializing_turtle()

    draw_tree(
        t=turtle_instance,
        length=start_length,
        angle_left=angle_left,
        angle_right=angle_right,
        depth=depth,
        scale=reduction_factor
    )

    screen.mainloop()

if __name__ == "__main__":
    main()
