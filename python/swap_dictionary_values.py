
# define key value pairs
dict_items = {"a": 1, "b": 2, "c": 3}


# swap values of a and b
tmp = dict_items["a"]

# Make first swap
dict_items["a"] = dict_items["b"]

# Make second, using tmp value
dict_items["b"] = tmp

print(dict_items)

# Define two variables
variable_1 = 1
variable_2 = 2

# swap values Pythonically
variable_1, variable_2 = variable_2, variable_1

# View result
print("variable_1:", variable_1)
print("variable_2:", variable_2)


# define key value pairs
d = {"a": 1, "b": 2, "c": 3}

# swap Pythonically
d["a"], d["b"] = d["b"], d["a"]

# view result
print("Result:", d)


# define key value pairs
d = {"a": 1, "b": 2, "c": 3}

# convert to a tuple
t = list(d.items())
print("Tuples:", t)

# swap order via index values
t[0], t[1] = t[1], t[0]
print("Swapped:", t)

# Convert back to dictionary
d = dict(t)
print("result:", d)

# define key value pairs
d = {"a": 1, "b": 2, "c": 3}

# swap values using Pythonic syntax
d["a"], d["b"] = d["b"], d["a"]

# view resut
print("result:", d)




