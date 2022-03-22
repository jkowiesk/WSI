def gray_to_dec(gray_num):
    """
    gray code to decimal converter for 5 bit arrays
    """
    binary_num = [gray_num[0]]
    for i, gray_bit in enumerate(gray_num[1:]):
        binary_num.append(binary_num[i] ^ gray_bit)
    dec_num = 0
    for bit in binary_num:
        dec_num = (2 * dec_num) + bit
    return dec_num - 16     # range of numbers < -16, 15 >


def genetic_to_dec(individual):
    x = []
    x_sections = [(0, 5), (5, 10), (10, 15), (15, 20)]
    for i in x_sections:
        x.append(individual[i[0]:i[1]])
    return [gray_to_dec(num) for num in x]


if __name__ == "__main__":
    print(gray_to_dec([1, 1, 0, 0, 1]))
