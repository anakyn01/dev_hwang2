abstract class Animal{//추상 클래스
    public abstract void ryusitae();
    public void song(){
        System.out.println("맞을래?");
    }
}

    //subclass
    class Nara extends Animal{
        public void ryusitae(){
            System.out.println("메롱 메롱 ~~");
        }
    }


        public class Abs_9 {
            public static void main(String[] args) {
                Nara parkNara = new Nara();
                /*클래스는 객체를 만들기위한 템플릿 템플릿으로 만드는 이유 언제든 필요에 의해 동일한 방법을 사용하는 컴포넌트화 시키기 위해서 */
                parkNara.ryusitae();
                parkNara.song();
            }
        }
/*
Java Abstraction
데이터 추상화는 특정세부정보를 숨기고 사용자에게 필수적인 정보만 표시하는 과정입니다
추상화는 추상클래스나 인터페이스를 통해 구현할수 있습니다
키워드 abstract[클래스와 매서드에 사용되는 비엑세스 수정자]을 사용합니다

추상클래스 : 객체를 생성하는데 사용 할수 없는 제한된 클래스
(이에 접근하려면 상속받아야 함)

추상 메소드 : 추상 클래스에서만 사용할수 있으며 본문이 없습니다
본문은 하위클래스(상속받은 클래스)에서 제공됩니다
 */