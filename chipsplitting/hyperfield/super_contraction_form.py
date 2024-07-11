def var_to_index(variable):
    """
    Converts a variable to an index in the contraction form.
    For example: x11 -> 5
    """
    base = 0
    offset = 0
    first_char = variable[0]
    if first_char == "x":
        base = 0
        second_char = variable[1]
        third_char = variable[2]
        offset = int(second_char) * 4 + int(third_char)
    elif first_char == "y":
        base = 16
        second_char = variable[1]
        third_char = variable[2]
        offset = int(second_char) * 4 + int(third_char)
    elif first_char == "z":
        base = 32
        second_char = variable[1]
        third_char = variable[2]
        offset = int(second_char) * 4 + int(third_char)
    elif first_char == "b":
        base = 48
        second_char = variable[1]
        offset = int(second_char)
    elif first_char == "c":
        base = 52
        second_char = variable[1]
        offset = int(second_char)
    elif first_char == "d":
        base = 56
        second_char = variable[1]
        offset = int(second_char)
    else:
        raise ValueError(f"Invalid variable {variable}")
    return base + offset


def index_to_var(index):
    """
    Converts a index to a variable in the contraction form.
    For example: 5 -> x11
    """
    if index < 16:
        char = "x"
        col = index // 4
        row = index % 4
        return f"{char}{col}{row}"

    if index < 32:
        char = "y"
        index -= 16
        col = index // 4
        row = index % 4
        return f"{char}{col}{row}"

    if index < 48:
        char = "z"
        index -= 32
        col = index // 4
        row = index % 4
        return f"{char}{col}{row}"

    if index < 52:
        char = "b"
        index -= 48
        return f"{char}{index}"

    if index < 56:
        char = "c"
        index -= 52
        return f"{char}{index}"

    if index < 60:
        char = "d"
        index -= 56
        return f"{char}{index}"

    raise ValueError(f"Invalid index {index}")
