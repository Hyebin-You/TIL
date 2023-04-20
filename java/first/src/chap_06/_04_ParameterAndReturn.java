package chap_06;

public class _04_ParameterAndReturn {
//    public static void power(int number) {
//        int result = number * number;
//        System.out.println(number + "의 2승은 " + result);
//    }

    public static int getPower(int number) {
        return number * number;
    }

//    public static void powerByExp(int number, int exponent) {
//        int result = 1;
//        for (int i = 0; i < exponent; i++) {
//            result *= number;
//        }
//        System.out.println(number + "의 " + exponent + "승은 " + result);
//    }

    public static int getPowerByExp(int number, int exponent) {
        int result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= number;
        }
        return result;
    }

    public static void main(String[] args) {
        // 전달값과 반환값이 있는 메소드
        int retVal = getPower(2);
        System.out.println(retVal);

        retVal = getPower(3);
        System.out.println(retVal);

        retVal = getPowerByExp(3, 3);
        System.out.println(retVal);
    }
}
