def hello(name):
    def hi(surname):
        print(f"Hello, {surname} {name}!")
    return hi


func = hello("Vlad")
func("Khimich")
