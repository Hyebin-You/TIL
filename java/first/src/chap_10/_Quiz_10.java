package chap_10;

import java.util.ArrayList;
import java.util.Arrays;

public class _Quiz_10 {
    public static void main(String[] args) {
//        int fee = 5000;
//        Customer[] customers = {new Customer("챈들러", 50),
//                new Customer("레이첼", 42),
//                new Customer("모니카", 21),
//                new Customer("벤자민", 18),
//                new Customer("제임스", 5)
//        };
//
//        System.out.println("미술관 입장료");
//        System.out.println("--------------------------");
////        Arrays.stream(customers).filter(x -> x.age >= 20).forEach(x -> System.out.println(x.name + " " + fee + "원"));
////        Arrays.stream(customers).filter(x -> x.age < 20).forEach(x -> System.out.println(x.name +" 무료"));

        ArrayList<Customer> list = new ArrayList<>();
        list.add(new Customer("챈들러", 50));
        list.add(new Customer("레이첼", 42));
        list.add(new Customer("모니카", 21));
        list.add(new Customer("벤자민", 18));
        list.add(new Customer("제임스", 5));

        System.out.println("미술관 입장료");
        System.out.println("--------------------------");
        list.stream()
                .map(x -> x.age >= 20 ? x.name + " 5000원" : x.name + " 무료")
                .forEach(System.out::println);
    }
}

class Customer {
    public String name;
    public int age;

    public Customer(String name, int age) {
        this.name = name;
        this.age = age;
    }
}