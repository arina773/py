def to_hex(number):
    remainders = []
    dict_ = {
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
        '5': 5, '6': '6', '7': '7', '8': '8', '9': '9',
        '10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e',
        '15': 'f',}
    quotient = 1
    while quotient != 0:
        remainders.append(number % 16)
        quotient = number // 16
        number = quotient
    final = ''
    for h in remainders[::-1]:
        final += dict_[str(h)]
    return final


def hex_color(red,green,blue):
    hex_color = '#'
    rgb_colors = [red, green, blue]
    for color in rgb_colors:
        c = to_hex(color)
        if len(c) == 1:
            hex_color += f'0{c}'
        else:
            hex_color += c           
    return hex_color
