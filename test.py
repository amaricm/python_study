def split_and_join(x):
    """
    This function is used to split and join strings
    it only works with variables of type string
    """
    a = x.split(" ")
    return "-".join(a)



print(split_and_join(2))