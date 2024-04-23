package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw11 frame = new MySw11();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySw11() {
		int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		for (int i = 0; i < 100; i++) {
			int rnd = (int)(Math.random() * 9);
			int temp = arr[0];
			arr[0] = arr[rnd];
			arr[rnd] = temp;
		}
		System.out.println("" + arr[0]+arr[1]+arr[2]);
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 281, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("야구게임");
		lbl.setBounds(29, 10, 64, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(105, 7, 127, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick(arr);
			}
		});
		btn.setBounds(29, 39, 203, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(29, 72, 203, 166);
		contentPane.add(ta);
	}
	
	void myClick(int[] arr) {
		int tf_num = Integer.parseInt(tf.getText());
		int a = tf_num/100;
		int b = tf_num%100/10;
		int c = tf_num%10;
		int[] my_arr = {a, b, c};
		
		int strike = 0;
		int ball = 0;
		
		for(int i =0; i < 3; i++) {
			for(int j =0; j < 3; j++) {
				if(arr[i] == my_arr[j]) {
					if(i == j) {
						strike++;
					} else {
						ball++;
					}
				}
			}
		}
		
		ta.setText("strike : " + strike + "\nball : " + ball);
		strike = 0;
		ball = 0;
		
	}
}
