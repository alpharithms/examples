"""
This file contains functions that can be used to generate random data such as
lists of fictitious employees.
"""
from random import choice


def create_random_people_data(count: int) -> list:
    """
    Creates a list of dict objects reflecting data representing an
    arbitrary number of records for fictitious persons in the following format:
    [
        {
            "id": "number",
            "first name": "f_name",
            "last name": "l_name",
            "location": {
                "city": "city_name",
                "state": "state_name"
            },
            "age": age
        },
        ...
    ]
    Returns:
        list of dict objects
    """
    # Define some attributes from which random data is generated
    f_names = ["Alice", "Bob", "John", "Mary", "Pat"]
    l_names = ["Smith", "Jones", "Williams", "Anderson", "Jacobs"]
    locations = [{"City": "Denver", "State": "Colorado"}, {"City": "Dallas", "State": "Texas"},
                 {"City": "Miami", "State": "Florida"}, {"City": "New York", "State": "New York"},
                 {"City": "Los Angeles", "State": "California"}]
    ages = [32, 18, 55, 60, 42, 24]

    # Generate <count> many random entries for people
    people = []
    for i in range(count):
        people.append(
            {
                "id": i + 1,
                "first_name": choice(f_names),
                "last_name": choice(l_names),
                "location": choice(locations),
                "age": choice(ages)
            }
        )
    return people
