class Add:

    @staticmethod
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

        negative = '-'
        if separator == '-':
            negative = '--'

        if negative in numbers:
            errorMessage = "Negative not allowed : "
            errorList = numbers.split(negative)
            for i in range(1, len(errorList)):
                error = errorList[i]
                foundNumber = error.split(separator)[0]
                errorMessage = errorMessage + "-" + foundNumber + ", "
            errorMessage = errorMessage[:-2]
            return errorMessage



        numbersum = 0
        if numbers == '':
            return '0'

        list_by_separator = numbers.split(separator)
        list_by_separator_and_newline = []
        for item in list_by_separator:
            if item == '' and list_by_separator.index(item) != len(list_by_separator) - 1:
                return "Error : 2 consecutive separators found"
            smalllist = item.split(r"\n")
            for item2 in smalllist:
                list_by_separator_and_newline.append(item2)

        if list_by_separator_and_newline[len(list_by_separator_and_newline)-1] == '':
            return 'Number expected but EOF found'

        for item in list_by_separator_and_newline:
            if item == '':
                return r"Number expected but '\n' found"

        for string in list_by_separator_and_newline:
            if Add.isfloat(string):
                numbersum += float(string)

        return str(numbersum)
