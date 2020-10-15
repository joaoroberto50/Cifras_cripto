
def _get_tables(table, a, b):
    for i in range(a, b):
        c = chr(i)
        table.append(c)
    return table

def ascii(a=32, b=128):
    if a < 32:
        a=32
    if b>128:
        b=128
    table = []
    table = _get_tables(table, a, b)
    table.append('\n')
    return table

def numbers():
    table = []
    table = _get_tables(table, 48, 58)
    return table

def lower_case(s = 1):
    table = []
    table = _get_tables(table, 97, 123)
    if s==1:
        table.append(' ')
        table.append('\n')
    return table

def up_case(s = 1):
    table = []
    table = _get_tables(table, 65, 91)
    if s==1:
        table.append(' ')
        table.append('\n')
    return table

def lower_n_up(s = 1):
    table = lower_case(s)
    table += up_case()
    table.pop()
    table.pop()
    return table

def lower_n_up_n_numbers(s = 1):
    table = lower_n_up(s)
    table += numbers()
    return table

def simbols():
    table = []
    table = _get_tables(table, 32, 48)
    table += ascii(58, 65)
    table += ascii(91, 97)
    table += ascii(123, 128)
    return table
