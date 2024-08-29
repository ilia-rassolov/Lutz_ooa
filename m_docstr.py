"I am: docstr.__ doc__"

def func(args):
    '''I am: docstr.func.__doc__'''
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__ doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)