class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER Parent altered()"

# assings dad to an instance of Parent
dad = Parent()
# assigns son to an instance of Child
son = Child()

# from dad calls the implicit function. This is not an override
dad.implicit()
# from son calls the parent's implicit function. This is not an override
son.implicit()

# from dad calls the override function. This is not an override
dad.override()
# from son calls the override function. This is an override
son.override()

# from dad calls the altered function. This is not an override
dad.altered()
# from son calls the altered function which is an override. Then calls the parent class' override function
son.altered()
