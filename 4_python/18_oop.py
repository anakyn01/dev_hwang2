class Student:
    #생성자 객체를 초기화 하는 형태 대량으로 생성하기 위해서 편리하게
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

pobj = Student("유지태", 27, 100000000)
hyi = Student("황영일",48, -1)

print(pobj.name, pobj.age)

oop = '''
클래스는 객체의 모양을 정의하고 객체는 해당 클래스를 기반으로 생성됩니다
class = 과일
object = 사과,바나나,망고

클래스와 객체를 사용하여 코드를 구성하여 구성과 재사용성을 개선할수 있다
- DRY원칙은 같은 코드를 한번이상 작성하지 않아야 한다는걸 의미합니다
반복되는 코드는 함수나 클래스로 옮겨 재사용 하세요
- 프로그램에 명확한 구조를 제공
- 코드를 유지관리,재사용,디버깅을 쉽게 만듭니다
- 불필요한 작업을 반족해서 하지 않는다
- 더적은 코드로 재사용 가능한 어플리케이션을 구축할수 있습니다
Don't Repeat Your self
what is OOP?
Object-Oriented Programing 객체지향 프로그래밍을 의미 합니다
'''