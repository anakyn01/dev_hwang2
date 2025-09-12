class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)#부모클래스에서 상속받음
        self.iam = year #자기 자신에 새로 추가되는 변수
#자식클래스 끝

x = Person("영일","황")
print(x.firstName , x.lastName)
print( x.lastName, x.firstName)

x = Student("mike","olsen", 2025)

#자식클래스 추가 파생클래스
'''
1)상속 => 재사용과 확장성
코드 재사용 ( reuse)
- 부모클래스의 속성(변수)과 기능(메서드)를 그대로 물려받아 사용하기 위함
- 기능확장(Extend) : 부모클래스에 없는 기능을 자식 새로 추가할수 있다
동물 - 강아지 멍멍()같은 메서드 추가
- 다형성(Polymorphism)활용
동물 a = new 강아지() 
동물 b = new 고양이()
같은 부모타입으로 여러 자식객체를 다루므로 코드의 유연성과 확장성이 높아진다

구조적 계층적 설계
복잡한 시스템을 부모 -> 자식 계층구조로 나눠 관리하면 이해하기 쉽고 확장이 용이
Vehicle
--car
--bicycle
'''


inheritance = '''
Python Inheritance
- 상속을 이용하면 부모클래스의 모든 메서드 와 속성을 객체에 상속 시킬수 있다
- 부모클래스 : 상속시키는 클래스로 기본 클래스라 합니다
- 자식클래스 : 부모클래스로 상속받은 클래스로 파생 클래스라고 합니다
'''