def my_reverse(l):
    reversed_list = []
    coursor = len(l) - 1
    while coursor > -1:
        reversed_list.append(l[coursor])
        coursor -= 1
    return reversed_list
