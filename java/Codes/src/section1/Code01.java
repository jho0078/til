package section1;

public class Code01 {

	public static void main(String[] args) {
		int x;
		x = 100;
		
		double y = 1.0023;
		
		// Person1은 하나의 타입이다
		Person1 first;
		first = new Person1(); // object
		
		first.name = "John";
		first.number ="01023456789";
		
		System.out.println("Name: " + first.name + ", Number: " + first.number);
		
		Person1 [] members = new Person1 [100];
		members[0] = first;
		members[1] = new Person1();
		members[1].name = "David";
		members[1].number = "01023454456"; 
		
		System.out.println("Name: " + members[1].name + ", Number: " + members[1].number);
		

	}

}
