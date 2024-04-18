package day03;

public class Human extends Animal {
	int skill_communication = 1;
	
	void momstouch(int stroke) {
		skill_communication += stroke;
	}
}
