from collections.abc import Iterable


def flatten(any_list) -> list:
    """
    Takes a multi-dimensional array of unknown depth and extracts
    single elements into a single dimensional list.

    Args:
        any_list: A list of unknown dimensions.
        
    Returns:
        Generator object representative of a 1-D flattened list
    """
    for element in any_list:
        if isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
            yield from flatten(element)
        else:
            yield element
