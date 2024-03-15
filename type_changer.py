def changer_type() -> any :
    """This function takes the value from the input and if the value is a number, it returns the number with its own type."""

    data = input('enter number : ')
    if data.isalpha() == True :
        raise TypeError ("The given value is not a number..!")

    try:
        if '.' in data:
            data1 = float(data)
            return data1
        else:
            data1 = int(data)
            return data1
    except:
        pass
        return data