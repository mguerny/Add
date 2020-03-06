class Add:

    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def add(numbers):

        # separator = numbers.split(r'\n')

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
            if Add.isfloat(string):
                numbersum += float(string)

        return str(numbersum)



