
from module_Human import Human
from module_Student import Student
from module_Group import Group, UserException


try:

    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print(gr)  # Only one student


except UserException as e:
    print(e)
