class Add:

    @staticmethod
    def add(numbers):
        numbersum = 0
        list_separated_by_comma = numbers.split(',')
        list_separated_by_newline_and_comma = []
        for item in list_separated_by_comma:
            smalllist = item.split(r"\n")
            for item2 in smalllist:
                list_separated_by_newline_and_comma.append(item2)
        for string in list_separated_by_newline_and_comma:
            if string.isnumeric():
                numbersum += int(string)

        return str(numbersum)



