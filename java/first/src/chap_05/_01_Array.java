package chap_05;

public class _01_Array {
    public static void main(String[] args) {
        // 배열 : 같은 자료형의 값 여러 개를 저장하는 연속된 공간
        String coffeeRoss = "아메리카노";
        String coffeeRachel = "카페모카";
        String coffeeChandler = "라떼";
        String coffeeMonica = "카푸치노";

        // 배열 선언 첫 번째 방법
//        String[] coffees = new String[4];

        // 두 번째 방법
        String coffee[] = new String[4];
        coffee[0] = coffeeRoss; // 인덱스는 0 부터 시작
        coffee[1] = coffeeRachel;
        coffee[2] = coffeeChandler;
        coffee[3] = coffeeMonica;

        // 세 번째 방법
//        String[] coffees = new String[] {"아메리카노", "카페모카", "라떼", "카푸치노"};

        // 네 번째 방법
        String[] coffees = {"아메리카노", "카페모카", "라떼", "카푸치노"};

        System.out.println("----------------------");

        // 커피 주문
        System.out.println(coffees[0] + "하나");
        System.out.println(coffees[1] + "하나");
        coffees[2] = "에스프레소";
        System.out.println(coffees[2] + "하나");
        System.out.println(coffees[3] + "하나");
        System.out.println("주세요");

        // 다른 자료형 ?
        int[] i = new int[3];
        i[0] = 1;
        i[1] = 2;
        i[2] = 3;
    }
}
