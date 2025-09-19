interface Animal{
    public void animalSound();
    public void time();
}
class Dogs implements Animal {
    public void animalSound(){
        System.out.println("강아지는 멍멍");
    }
    public void time(){
        System.out.println("사람에 한시간은 강아지에게 반나절");
    }
}

public class Dog{
    public static void main(String[] hyi) {
        Dogs dogs = new Dogs();
        dogs.animalSound();
        dogs.time();
    }
}

/*
자바에서 추상화를 달성하는 또다른 방법은
인터페이스를 사용하는 것 입니다

본문으로 관련 매서드를 그룹화하는 추상클래스 입니다
 */
