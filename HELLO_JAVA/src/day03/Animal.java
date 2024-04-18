package day03;

public class Animal {
	boolean flagM = true;
	
	void goToThai() {
		flagM = !flagM;
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println("1: " + ani.flagM);
		ani.goToThai();
		System.out.println("1: " + ani.flagM);
	}
}
