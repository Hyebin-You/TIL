package chap_10.convertor;

@FunctionalInterface
public interface Convertible {
    // 인터페이스에는 하나의 메소드만
    void convert(int USD);
}
