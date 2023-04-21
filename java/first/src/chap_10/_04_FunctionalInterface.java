package chap_10;

import chap_10.convertor.Convertible;
import chap_10.convertor.KRWConvertor;

public class _04_FunctionalInterface {
    public static void main(String[] args) {
        KRWConvertor converter = new KRWConvertor();
//        converter.convert(2);

//        convertUSD(USD -> System.out.println(USD + " 달러 = " + (USD * 1400) + " 원"), 2);

        Convertible convertible = USD -> System.out.println(USD + " 달러 = " + (USD * 1400) + " 원");
        convertUSD(convertible, 1);


        // 전달값이 하나도 없다면?
    }

    public static void convertUSD(Convertible converter, int USD) {
        converter.convert(USD);
    }
}
