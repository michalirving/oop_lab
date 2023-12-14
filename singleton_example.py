class SingletonExample(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instace = super().__call__(*args, **kwargs)
            cls._instances[cls] = instace
            # print(cls._instances[cls])
            # print(cls._instances)
        return cls._instances[cls]


class Example(metaclass=SingletonExample):
    def __init__(self):
        self.value = 1

    
    
example_1 = Example()
example_2 = Example()

example_1.value = 2
example_2.value = 4

print(example_1.instace)
print(example_2.instace)

