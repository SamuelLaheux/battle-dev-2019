from random import randint


def generate_csv_input_file(filename="data/ex2.csv"):
    """Generates csv input file.

    Args:
        filename (string): Name of csv file to generate. Defaults to "data/ex2.csv".

    Returns:
        Nothing

    """
    nb_frames = 4
    res = []
    for i in range(nb_frames):
        length_wood = randint(1, 1000)
        res.append(f"{length_wood}\n")

    with open(filename, "w") as f:
        f.writelines(res)


def wasted_centimeters_of_wood(filename="data/ex2.csv"):
    """From csv input file, returns the number of wasted centimeters of wooden frames.

    :Example:

    Csv Input File:
        633
        945
        521
        967

    >>> wasted_centimeters_of_wood()
    982

    Args:
        filename (string): Name of csv input file. Defaults to "data/ex2.csv".

    Returns:
        string: Returns the number of wasted centimeters of wooden frames.

    """
    with open(filename, "r") as f:
        data = f.readlines()

    y_list = [int(d.rstrip("\n")) for d in data]
    res = sum(y_list) - 4 * min(y_list)

    return res


if __name__ == "__main__":
    generate_csv_input_file()
    print(wasted_centimeters_of_wood())
