class CustomMeta(type):

    def __new__(mcs, classname, method, attrs):
        attributes = {}
        for classname, value in attrs.items():
            attributes[classname.lower() + ("method")] = value
        return type(classname, method, attrs)


class Test(metaclass=CustomMeta):
    name = "Some_name"
    def get_name(self):
        print(self.name)

if __name__ == "__main__":
    a = Test()
    print(a)

    
#про патерни прочитала ваші матеріали + ті, що знайшла самостійно 
