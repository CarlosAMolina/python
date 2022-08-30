class Foo:
    class_attribute = "Class attribute"

    def __init__(self):
        self.instance_attribute = "Instance attribute"

    def instance_method(self):
        """Intance methods can access the class instance."""
        print(self.class_attribute)
        print(self.instance_attribute)

    @classmethod
    def class_method(cls):
        """Class methods can access the class itself.

        They cannot access the class instance.
        """
        print(cls.class_attribute)


# Instance methods need a class instance.
Foo().instance_method()


# Class methods don't need a class instance.
Foo().class_method()
Foo.class_method()
