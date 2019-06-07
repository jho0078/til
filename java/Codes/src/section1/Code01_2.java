package section1;

public class Code01_2 {

	public static void main(String[] args) {
		
		Person1 first;
		first = new Person1(); // object
		
		first.name = "John";
		first.number ="01023456789";
		
		System.out.println("Name: " + first.name + ", Number: " + first.number);
		
		// first�� second�� ���� ���� ����
		Person1 second = first;
		System.out.println("Name: " + second.name + ", Number: " + second.number);
		
		// second�� �ٲٸ� first�� ���� �ٲ��.(���� ���� �����ϰ� �ֱ� ����)
		second.name = "Tom";
		System.out.println("Name: " + first.name + ", Number: " + first.number);

		// �迭�� �� ĭ�� Person1 Ÿ��
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
