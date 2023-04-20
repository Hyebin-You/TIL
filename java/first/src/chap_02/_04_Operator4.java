package chap_02;

public class _04_Operator4 {
    public static void main(String[] args) {
        // 논리 연산자
        boolean kimchi = false;
        boolean egg = false;
        boolean pork = true;

        System.out.println(kimchi || egg || pork); // true
        System.out.println(kimchi && egg && pork); // false

        // And 연산
        System.out.println((5 > 3) && (3 > 1)); // true
        System.out.println((5 > 3) && (3 < 1)); // false

        // Or 연산
        System.out.println((5 > 3) || (3 > 1)); // true
        System.out.println((5 > 3) || (3 < 1)); // true
        System.out.println((5 < 3) || (3 < 1)); // false

        // 논리 부정 연산자
        System.out.println(!true); // false
        System.out.println(!false); // true
        System.out.println(!(5 == 5)); // false
    }
}
