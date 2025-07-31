def percentage_change(start, end):
    """
    i have no idea how neither python nor pandas doesn't have a builtin percentage calculation, so i made one myself
    this one calculates the percentage that the value have changes from the start to the end
    :param start: what the value was before the change
    :param end: the value after the change
    :return: how much the value was changed in percentage
    """
    return (end - start) / start * 100