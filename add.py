class Add:

    @staticmethod
    def add(numbers):
        numbersum = 0
        if numbers == '':
            return '0'

        list_by_separator = numbers.split(',')
        list_by_separator_and_newline = []
        for item in list_by_separator:
            smalllist = item.split(r"\n")
            for item2 in smalllist:
                list_by_separator_and_newline.append(item2)

        for item in list_by_separator_and_newline:
            if item == '':
                return 'Number expected but EOF found'

        for string in list_by_separator_and_newline:
            if string.isnumeric():
                numbersum += int(string)

        return str(numbersum)


