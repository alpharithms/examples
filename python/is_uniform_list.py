def is_uniform_list(items: list) -> bool:
    """
    Given a list, determines if elements are of equal length.
    Returns:
        True if elements are all of equal length else False
    """
    return not any(len(x) != len(y) for x in items for y in items if x is not y)
