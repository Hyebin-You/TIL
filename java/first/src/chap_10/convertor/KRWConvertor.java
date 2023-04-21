package chap_10.convertor;

public class KRWConvertor implements Convertible {

    @Override
    public void convert(int USD) {
        System.out.println(USD + " 달러 = " + (USD * 1400) + " 원");
    }
}
