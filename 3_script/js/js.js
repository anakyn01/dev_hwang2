//2)let, const
const PI = 3.141592653589793;
//PI = 3.14; let과 const는 재할당을 금지합니다
document.write(PI);


let a = 2;//재선언 재할당 금지
//그러나 다른 블록에서는 재선언이 가능하다
{
 let a = 3;
 //같은 블록에서 한번씩만 가능합니다
 //그러나 출력은 최초에 설정했던 변수의 값을 출력합니다
}
document.write(a + "<br/>");

//1)문
let x, y, z;//변수 x,y,z선언
x = 5;//변수x에 값 5를 대입
y = 6;//변수 y에 6을 대입
z = x + y;//11

document.write(z);//도큐먼트에 변수g를 쓰세요

//문자열 변수 
let firstName = "영일";
let lastName = "황";

document.write("저의 이름은 " + lastName + firstName + " 입니다");

