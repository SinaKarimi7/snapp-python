def inspect(func):
    def wrapper_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        result = func(*args)
        print(f"Function execution completed. Result: {result!r}")
        return result
    return wrapper_func

@inspect
def combine(a, b):
    return a + b

class User:
    user_registry = {}
    @classmethod
    def create_user(cls, name):
        user = User.user_registry.get(name)
        if user is not None: return user
        return cls(name)

    def __init__(self, name):
        print(f'__init__: {id(self)}')
        self.name = name
        self.credit = 0
        User.user_registry[self.name] = self

    def change_name(self, new_name):
        print(f'change_account: {id(self)}')
        self.name = new_name

    @property
    def title(self): return 'Mr./Mrs. ' + self.name
    pass
class SpecialUser(User):
    pass

ali = User.create_user('Ali')
print(f'ali: After creation: {id(ali)}, {type(ali)}')
ali2 = User.create_user('Ali')
print(f'ali2: After creation: {id(ali2)}, {type(ali2)}')
ziba = SpecialUser.create_user('Ziba')
print(f'ziba: After creation: {id(ziba)}, {type(ziba)}')

print(f'ziba.name: {ziba.name}')
print(f'ziba.title: {ziba.title}')

ali.change_name('Mr. Ali')

copy_of_ali = ali
