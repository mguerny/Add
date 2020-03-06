class Add:

    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def add(numbers):

        separator = ','

        if '//' in numbers:
            if numbers[0] == '/' and numbers[1] == '/':
                separator = numbers.split(r"\n")[0][2:]
                if separator == ".":
                    return "'.' not allowed as separator"
                len_to_remove = 2 + len(separator) + 2
                numbers = numbers[len_to_remove:]

        numbersum = 0
        if numbers == '':
            return '0'

        list_by_separator = numbers.split(separator)
        list_by_separator_and_newline = []
        for item in list_by_separator:
            smalllist = item.split(r"\n")
            for item2 in smalllist:
                list_by_separator_and_newline.append(item2)

        for item in list_by_separator_and_newline:
            if item == '':
                return 'Number expected but EOF found'

        for string in list_by_separator_and_newline:
            if Add.isfloat(string):
                numbersum += float(string)

        return str(numbersum)





