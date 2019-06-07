package section1;

public class Code01_2 {

	public static void main(String[] args) {
		
		Person1 first;
		first = new Person1(); // object
		
		first.name = "John";
		first.number ="01023456789";
		
		System.out.println("Name: " + first.name + ", Number: " + first.number);
		
		// first와 second는 같은 곳을 참조
		Person1 second = first;
		System.out.println("Name: " + second.name + ", Number: " + second.number);
		
		// second를 바꾸면 first도 같이 바뀐다.(같은 곳을 참조하고 있기 때문)
		second.name = "Tom";
		System.out.println("Name: " + first.name + ", Number: " + first.number);

		// 배열의 각 칸은 Person1 타입
		Person1 [] members = new Person1 [100];
		members[0] = first;
		members[1] = second;
		System.out.println("Name: " + members[1].name + ", Number: " + members[1].number);

		
		members[2] = new Person1();
		members[2].name = "David";
		members[2].number = "01023454456"; 
		
		System.out.println("Name: " + members[1].name + ", Number: " + members[1].number);

	}

}
