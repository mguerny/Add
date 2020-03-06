class Add:

    @staticmethod
    def add(numbers):
        numbersum = 0
        liststringtemp = numbers.split(',')
        liststring = []
        for item in liststringtemp:
            smalllist = item.split(r"\n")
            for item2 in smalllist:
                liststring.append(item2)
        for string in liststring:
            if string.isnumeric():
                numbersum += int(string)

        return str(numbersum)



