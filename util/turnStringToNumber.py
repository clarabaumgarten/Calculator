def turns_string_number_to_float(string_number):
    if string_number not in ('-', '+', '*', '/', '**', '//'):
        return float(string_number)
    return string_number
