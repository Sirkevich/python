class A:
    def show(self):
        return "A"


class B(A):
    def show(self):
        return "B"


class C(B):
    def show(self):
        return "C"


class D(C):
    def show(self):
        return "D"



obj_A = A()
output_A = capture_stdout(obj_A.show)
assert output_A == "A"
