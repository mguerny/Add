class Add:

    @staticmethod
    def add(numbers):
        if numbers == '':
            return '0'

        if len(numbers) == 1 and numbers.isnumeric():
            return numbers

        if len(numbers) == 3:
            s1 = numbers[0]
            s2 = numbers[2]
            if s1.isnumeric and s2.isnumeric():
                return str(int(s1) + int(s2))

        if len(numbers) == 5:
            s1 = numbers[0]
            s2 = numbers[2]
            s3 = numbers[4]
            if s1.isnumeric and s2.isnumeric() and s3.isnumeric():
                return str(int(s1) + int(s2) + int(s3))


