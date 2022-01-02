import re
import math
from typing import Union, List, Dict


def move_zeros(given_list: list[int]) -> list[int]:
    """Move zero at the end of given list

    Args:
        given_list (list[int]): List of elements to process

    Returns:
        list[int]: List processed
    """
    return [*[n for n in given_list if n != 0], *[0] * given_list.count(0)]


assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
assert move_zeros([1, 0, 0, 2, 0, 1, 3]) == [1, 2, 1, 3, 0, 0, 0]
assert move_zeros([0, 0, 1, 0, 0, 1, 0]) == [1, 1, 0, 0, 0, 0, 0]


def square(number: int) -> int:
    """Square every digit of a number and concatenate them.

    Args:
        n (int): number to process

    Returns:
        int: result
    """
    return int("".join([f"{int(n)**2}" for n in str(number)]))


assert square(9119) == 811181
assert square(3212) == 9414
assert square(2112) == 4114
assert square(0) == 0


def count_duplicate(string: str) -> int:
    """The count of distinct case-insensitive alphabetic characters
    and numeric digits that occur more than once in the input string

    Args:
        string (str): string to processed

    Returns:
        int: number of duplicates
    """
    duplicates: list[str] = []
    for s in string.lower():
        if string.lower().count(s) > 1 and s not in duplicates:
            duplicates.append(s)
    return len(duplicates)


assert count_duplicate("product") == 0
assert count_duplicate("indivisibility") == 1
assert count_duplicate("tests") == 2
assert count_duplicate("mathematics") == 3


def is_square(number: int) -> bool:
    """Given an integral number, determine if it's a square number
        In mathematics, a square number or perfect square is an integer
        that is the square of an integer;
        in other words, it is the product of some integer with itself.

    Args:
        number (int): number to test

    Returns:
        bool: result
    """
    try:
        return math.sqrt(number).is_integer()
    except ValueError:
        return False


assert is_square(0) is True
assert is_square(-1) is False
assert is_square(4) is True
assert is_square(25) is True


def dna(string: str) -> str:
    """Deoxyribonucleic acid (DNA)

    Args:
        string (str): string to process

    Returns:
        str: dna result
    """
    complements: dict[str, str] = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complements[s.upper()] for s in string])


assert dna("ATTGC") == "TAACG"
assert dna("GTAT") == "CATA"
assert dna("ATGC") == "TACG"
assert dna("AAAA") == "TTTT"


def sum_of(a: int, b: int) -> int:
    return sum(range(min([a, b]), max([a, b]) + 1))


assert sum_of(1, 0) == 1
assert sum_of(1, 2) == 3
assert sum_of(0, 1) == 1
assert sum_of(1, 1) == 1
assert sum_of(-1, -1) == -1
assert sum_of(-1, 2) == 2
assert sum_of(0, -1) == -1


def maskify(string: str) -> str:
    """Changes all but the last four characters into '#'

    Args:
        string (str): string to process

    Returns:
        str: string processed
    """
    return "#" * len(string[0:-4]) + string[-4:]
    # return "".join(["#" if len(string) > 4 else s for s in string[0:-4]]) + string[-4:]


assert maskify("4556364607935616") == "############5616"
assert maskify("64607935616") == "#######5616"
assert maskify("1") == "1"
assert maskify("") == ""


def divisors(number: int) -> Union[list[int], str]:
    """Find the divisors!

    Args:
        number (int): number to process

    Returns:
        Union[list[int], str]: divisors or str 'is prime'
    """
    return [i for i in range(2, number) if not number % i] or f"{number} is prime"


assert divisors(4) == [2]
assert divisors(12) == [2, 3, 4, 6]
assert divisors(1) == "1 is prime"
assert divisors(5) == "5 is prime"


def to_camel_case(string: str) -> str:
    """Convert string to camel case

    Args:
        string (str): text to process

    Returns:
        str: result
    """
    return "".join(
        [
            word.capitalize() if index != 0 else word
            for index, word in enumerate(re.split("_|-", string))
        ]
    )


assert to_camel_case("") == ""
assert to_camel_case("is_prime") == "isPrime"
assert to_camel_case("a-girl-has-no-name") == "aGirlHasNoName"
assert to_camel_case("Yes_my_lord") == "YesMyLord"
assert to_camel_case("My-class") == "MyClass"


def get_embedded_attributes(
    list_attributes: List[str],
) -> Dict[str, Union[List[str], Dict[str, List[str]]]]:
    """Separate embedded attributes to normal ones

    Args:
        list_attributes (List[str]): list of attributes to process

    Returns:
        Dict[str, Union[List[str], Dict[str, List[str]]]]:
        ex: {"embed": {"key": ["attr1", attr2]}, "attributes": ["attr3", "attr4"]}
    """
    """
    from functools import reduce

    def f(
        acc: Dict[str, Union[List[str], Dict[str, List[str]]]], value: str
    ) -> Dict[str, Union[List[str], Dict[str, List[str]]]]:

        if "." in value:

            acc["embed"][value.split(".")[0]] = [
                *acc["embed"].get(value.split(".")[0], []),
                value.split(".")[1],
            ]

        else:
            acc["base"] = [*acc["base"], value]

        return acc

    r = reduce(f, list_attributes, {"base": [], "embed": {}})
    print("________________________________________________________________")
    print(r)
    print("________________________________________________________________")
    return r
    """
    embedded_attrs = [
        (attr.split(".")) for attr in filter(lambda attr: "." in attr, list_attributes)
    ]
    # assert all([len(attrs) == 2 for attrs in embedded_attrs]) is True

    res: Dict[str, Union[List[str], Dict[str, List[str]]]] = {
        "base": list(filter(lambda attr: "." not in attr, list_attributes)),
        "embed": {},
    }

    # assert all(["." not in attr for attr in res["attributes"]]) is True

    for embed_attr in embedded_attrs:
        res["embed"][embed_attr[0]] = [
            *res["embed"].get(embed_attr[0], []),
            embed_attr[1],
        ]
    return res


assert get_embedded_attributes(
    [
        "questionnaire.questionnaire_name",
        "questionnaire.created_at",
        "title",
        "slug",
        "modified_at",
    ]
) == {
    "embed": {"questionnaire": ["questionnaire_name", "created_at"]},
    "base": ["title", "slug", "modified_at"],
}

assert get_embedded_attributes(
    [
        "questionnaire.questionnaire_name",
        "questionnaire.created_at",
        "title",
        "comment.content",
        "user.last_name",
        "user.first_name",
    ]
) == {
    "embed": {
        "questionnaire": ["questionnaire_name", "created_at"],
        "comment": ["content"],
        "user": ["last_name", "first_name"],
    },
    "base": ["title"],
}

print("All tests passed [OK]")
