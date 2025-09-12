/*
public : 접근제어자 프로젝트내 어디서든 접근 가능함
class : 클래스를 정의 한다는 키워드
Intro_1 : 클래스명은 최초 작성한 파일명과 완전 동일해야 합니다

Intro_1이라는 이름을 가진 공개 클래스 선언
 */

public class Intro_1 {
    

    public static void main(String[] args){

        int num = 10; //여기서 10 정수리터럴
        String message = "곧 쉬는시간";
        boolean isActive = true; //ture

        System.out.println(num);
        System.out.println(message);
        System.out.println(isActive);
        System.out.println("hello world");
/*
System : 자바의 표준 라이브러리 클래스 (java.lang.System)
out : System 클래스가 제공하는 정적(static)출력 스트림(PrintStream)
println() 출력후 줄바꿈을 하는 메서드
"Hell0 world" 문자열 리터럴
*/ 
    }
}
/*
public : 어디서나 호출가능해야 
하므로 공개 접근제어자 사용
static : 객체를 생성하지 않아도 실행할수 있도록 함 jvm이
클래스 로딩후 바로 실행가능
void : 리턴값 없음 
리턴이 들어가면 변수 타입이 붙는다
main : 프로그램 시작점(entry point)로 인식되는 메서드 이름
(String[] args) : 명령줄 인자(command line arguments)를
배열로 전달받음

즉 프로그램 실행이 시작되는 특별한 메소드 정의
팩키지 패키지
 */