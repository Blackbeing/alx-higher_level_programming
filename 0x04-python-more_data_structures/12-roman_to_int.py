#!/usr/bin/python3

def match_func(roman_nums, string):
    value = 0
    for roman_num in roman_nums:
        if string[:len(roman_num[0])] == roman_num[0]:
            value += roman_num[1]
            return value, len(roman_num[0])
    return (0, 0)


def thousands(string):
    roman_nums = [("M", 1000)]
    return match_func(roman_nums, string)


def hundreds(string):
    roman_nums = [
            ("D", 500), ("CM", 900), ("CD", 400), ('C', 100)]
    return match_func(roman_nums, string)


def tens(string):
    roman_nums = [
            ("L", 50),
            ("XL", 40), ("XC", 90), ('X', 10)
    ]
    return match_func(roman_nums, string)


def ones(string):
    roman_nums = [("IX", 9), ("IV", 4), ("V", 5), ("I", 1)]
    return match_func(roman_nums, string)


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    temp_str = roman_string
    number = 0

    while (temp_str):
        value, step = thousands(temp_str)
        if value:
            number += value
            temp_str = temp_str[step:]
            continue

        value, step = hundreds(temp_str)
        if value:
            number += value
            temp_str = temp_str[step:]
            continue

        value, step = tens(temp_str)
        if value:
            number += value
            temp_str = temp_str[step:]
            continue

        value, step = ones(temp_str)
        if value:
            number += value
            temp_str = temp_str[step:]
    return number
