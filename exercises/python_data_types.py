from termios import VLNEXT


def is_bool(value):
    return isinstance(value, bool)


def is_int(value):
    return isinstance(value, int)


def is_float(value):
    return isinstance(value, float)


def is_string(value):
    return isinstance(value, str)


def is_list(value):
    return isinstance(value, list)


def is_tuple(value):
    return isinstance(value, tuple)


def is_set(value):
    return isinstance(value, set)


def is_dict(value):
    return isinstance(value, dict)


def return_lower_case_string(word: str):
    return word.lower()


def append_element_in_list(element, input_list: list):
    input_list.append(element)
    return input_list


def remove_element_from_list(element, input_list: list):
    input_list.remove(element)
    return input_list


def create_new_key_value_in_dict(key, value, input_dict):
    return


def delete_key_from_dict(key, input_dict):
    return


def add_element_to_set(element, input_set):
    return


def remove_element_from_set(element, input_set):
    return
