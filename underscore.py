class Underscore:       # a python "module" is a group of functions (def) inside a single class
    def map(self, lis, callback):
        arr = []
        for i in lis:
            arr.append(callback(i))
        return arr
    def find(self, lis, callback):
        for i in lis:
            if callback(i):
                return i
    def filter(self, lis, callback):
        arr = []
        for i in lis:
            if callback(i):
                arr.append(i)
        return arr
    def reject(self, lis, callback):
        arr = []
        for i in lis:
            if not callback(i):
                arr.append(i)
        return arr
_ = Underscore()

doubles = _.map([1,2,3,45], lambda x: x*2)
greater4 = _.find([1,2,3,4,-95,996], lambda x: x>4)
evens = _.filter([1, 2, 3, 4, 5, 6, -56], lambda x: x%2 == 0)
not_evens = _.reject([1,2,3,4,5,6,-55], lambda x: x%2 == 0)

print("'map' to print doubles = ", doubles)
print("'find' to print first number greater than 4 = ", greater4)
print("'filter' to print evens = ", evens)
print("'reject' to print non-evens = ", not_evens)
