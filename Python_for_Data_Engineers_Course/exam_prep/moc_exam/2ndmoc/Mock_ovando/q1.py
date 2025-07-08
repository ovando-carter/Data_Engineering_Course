def rightAngledTriangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:

        return False
    elif a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return True 
    else:
        return False
