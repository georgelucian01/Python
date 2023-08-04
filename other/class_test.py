

class A:
    def __new__(cls, *args, **kwargs):
        print('new', cls, args, kwargs)
        return super().__new__(cls)
    
    def __init__(self, *args, **kwargs):
        print('init', self, args, kwargs)

    
def how_object_construction_works():
    x = A(1, 2, 3, x=4)


def main(): 
    how_object_construction_works()
    
if __name__ == "__main__":
    main()