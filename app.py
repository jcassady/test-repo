class Y:  # Short, cryptic class name
    def __call__(self, *args):  # Call method, minimalistic
        print(f"{' '.join(args[::-1])}")  # Reversing and printing args

Y()("World!", "Hello")  # Instantiating and calling in one go
