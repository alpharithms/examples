def simple_take(iterable, indices, mode: str = 'wrap'):
    """
    Emulates the basic functions of NumPy.take() to retrieve
    the specified indices of a collection where out-of-bounds
    values are substituted using the `mode` type.

    Args:
        mode: str - 'wrap' or 'clip'. Default is 'wrap'
        iterable: Any - an iterable object
        indices: Collection - a collection of values representing
            index values from which to extract values from iterable.

    Returns:
        A collection of values from iterable
    """
    iter_length = len(iterable)
    output = []
    for i in indices:
        if i < iter_length:
            output.append(iterable[i])
        elif mode == 'wrap':
            output.append(iterable[i % iter_length - 1])
        elif mode == 'clip':
            output.append(iterable[-1])
    return output
