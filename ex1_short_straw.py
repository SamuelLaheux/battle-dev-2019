from random import randint, choice
from string import ascii_lowercase


def generate_csv_input_file(filename="data/ex1.csv"):
    """Generates csv input file.

    Args:
        filename (string): Name of csv file to generate. Defaults to "data/ex1.csv".

    Returns:
        Nothing

    """
    with open(filename, "w") as f:
        nb_people = randint(10, 100)
        res = [f"{nb_people}\n"]
        for i in range(nb_people):
            length_name = randint(5, 10)
            name = "".join(choice(ascii_lowercase) for i in range(length_name))
            length_wood = randint(1, 1000)
            res.append(f"{name} {length_wood}\n")
        f.writelines(res)


def who_has_the_smallest(filename="data/ex1.csv"):
    """From csv input file, returns the name of the person who have the smallest straw.

    :Example:

    Csv Input File:
        3
        alice 45
        bruno 21
        camille 67

    >>> who_has_the_smallest()
    bruno

    Args:
        filename (string): Name of csv input file. Defaults to "data/ex1.csv".

    Returns:
        string: Returns the name of the person who have the smallest straw.

    """
    with open(filename, "r") as f:
        data = f.readlines()
        data_format = [d.rstrip("\n") for d in data]
        data_format.pop(0)
        res = [{e.split(" ")[0]: int(e.split(" ")[1])} for e in data_format]
        dictionary = {k: v for list_item in res for (k, v) in list_item.items()}
        min_length_wood = min([list(r.values())[0] for r in res])

    for name, length_wood in dictionary.items():
        if length_wood == min_length_wood:
            name_to_return = name
            return name_to_return


if __name__ == "__main__":
    generate_csv_input_file()
    print(who_has_the_smallest())
