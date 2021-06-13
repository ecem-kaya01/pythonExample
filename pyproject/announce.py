def announce(f):
    def wrapper():
        print("Loading...")
        f()
        print("Succsesfully announced!")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()