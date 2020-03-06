class Add:

    @staticmethod
    def add(numbers):
        numbersum = 0
        liststring = numbers.split(',')
        for string in liststring:
            if string.isnumeric():
                numbersum += int(string)

        return str(numbersum)


