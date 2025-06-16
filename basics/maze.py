def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
        if wall_in_front():
           turn_left()
    elif wall_in_front() and not wall_on_right():
        turn_right()
    elif not wall_in_front() and wall_on_right():
        move()
        turn_left()
        if wall_in_front():
            turn_right()
    else:
        move()
            

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
