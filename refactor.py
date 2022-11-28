1.def to_camel_case(text):
    return (re.sub(r"\s+", "", re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|" "|-', text)[1::])))

2.class SingletonMeta(type):

    _instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            cls._instances[cls] = super().call(*args, **kwargs)
        return cls._instances[cls]

class MetaType(metaclass=SingletonMeta):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Type {self.name}'


3.count_bits = lambda n: bin(n).count('1')

4.def digital_root(n):
    return (n if n < 10  else digital_root(sum(map(int,str(n)))))

5.even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
