def rightAngledTriangle(a, b, c):
    # make sure that the sides are greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # make sure that no matter the order of the argument that it adhers to pythagoras therim
    elif a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return True 

    # if the requirements are not met then it is not a right angle triangle
    else:
        return False
