
class FizzBuzz:

    def outputForNumber(self, i):
        output = ''

        if i % 3 == 0: 
            output += 'fizz'
        if i % 5 == 0: 
            output += 'buzz'
        if not output: 
            output = str(i)

        return output

    def printOutputForNumber(self, i):
        print self.outputForNumber(i)