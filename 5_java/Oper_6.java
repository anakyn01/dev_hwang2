/*
자바 연산자
변수와 값에 대한 연산을 수행하는데 사용됩니다
산술 연산자
+ - * / % ++ --

할당 연산자
= += -= *= /= %= |= ^= >>= <<=
비교 연산자
논리 연산자
비트 연산자
 */

public class Oper_6 {
    
    public static void main(String[] args) {
//4)논리 연산자 : 두가지 조건이 다 맞거나 둘중에 하나만 맞거나 같지않거나
//&& and 
int a = 5; System.out.println( a > 3 && a < 10);
//|| or
int s = 5; System.out.println( s == 5 || s < 1);

//Logical not 틀리면 true 같으면 false
System.out.println("=============");
int g = 5;
System.out.println(!(g < 5 && g > 6));


//3)비교 연산자 : 비교 연산자는 두값을 비교하는데 사용
//이는 프로그래밍에서 아주 중요합니다 답을 찾고 결정을 내리는 데 도움이 되기 때문입니다
int u = 5; int p =3; System.out.println( u > p);
int i = 5; int o = 5; System.out.println(i == o);

int age = 18;
System.out.println(age >= 18);
System.out.println(age < 18);

int passwordLength = 5;
System.out.println(passwordLength >= 8);
System.out.println(passwordLength <= 8);


//2)할당 연산자 : 변수에 값을 할당하는데 사용합니다
int q = 10; q += 5; System.out.println(q);
double w = 5; w /=3; System.out.println(w);
int e = 6; e /= 3; System.out.println(e);
int r = 7; r %= 2; System.out.println(r);

  //1)산술연산자
  int x = 10; int y =3; 
  System.out.print(x + y);  
  System.out.print(x - y); 
  System.out.print(x * y); 
  System.out.print(x / y); 
  System.out.print(x % y); 


  
  //전위연산자(Pre[변수값을 먼저 변경하고 사용]) 조건 확인전에 값을 미리 증가시킬때 
  //와 후의연산자(Post[변수 값 사용 변경]) 에 차이 현재 값은 쓰되 이후 자동 증가가 필요할때
int z = 5;
++z;//1씩 증가
  System.out.println(z);
--z;
  System.out.println(z);
  
//갑자기 변수[많은수여서 변수 변하는 수여서 변수] 명이 이해가안 될때
int peopleInRoom = 0; //변화는 기준에 초기 설정을 해주는것을 변수 초기화 
//3명이 들어옴
peopleInRoom++;
peopleInRoom++;
peopleInRoom++;

System.out.println(peopleInRoom);

//한명에 중탈
peopleInRoom--;
System.out.println(peopleInRoom);


}
}
