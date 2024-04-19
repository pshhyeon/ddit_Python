package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;

public class MySw05 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw05 frame = new MySw05();
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
	public MySw05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl01 = new JLabel("__");
		lbl01.setBounds(27, 10, 40, 15);
		contentPane.add(lbl01);
		
		JLabel lbl02 = new JLabel("__");
		lbl02.setBounds(94, 10, 40, 15);
		contentPane.add(lbl02);
		
		JLabel lbl03 = new JLabel("__");
		lbl03.setBounds(161, 10, 40, 15);
		contentPane.add(lbl03);
		
		JLabel lbl04 = new JLabel("__");
		lbl04.setBounds(228, 10, 40, 15);
		contentPane.add(lbl04);
		
		JLabel lbl05 = new JLabel("__");
		lbl05.setBounds(295, 10, 40, 15);
		contentPane.add(lbl05);
		
		JLabel lbl06 = new JLabel("__");
		lbl06.setBounds(362, 10, 40, 15);
		contentPane.add(lbl06);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int[] arr = myClick();
				// 클래스에 전역으로 설정하는 방법도 있지만 여기서는 배열을 반환받아서 사용했음
				lbl01.setText(String.valueOf(arr[0]));
				lbl02.setText(String.valueOf(arr[1]));
				lbl03.setText(String.valueOf(arr[2]));
				lbl04.setText(String.valueOf(arr[3]));
				lbl05.setText(String.valueOf(arr[4]));
				lbl06.setText(String.valueOf(arr[5]));
			}
		});
		btn.setBounds(12, 48, 390, 23);
		contentPane.add(btn);
	}
	
	int[] myClick() {
		int[] arr = {
		       1,  2,  3,  4,  5,  6,  7,  8,  9, 10
		    , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
		    , 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
		    , 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
		    , 41, 42, 43, 44, 45
		};
		
		for (int i = 0; i < 1000; i++) {
			int rnd = (int)(Math.random()*45);
			int temp = arr[0];
			arr[0] = arr[rnd];
			arr[rnd] = temp;
		}
		
		// 확인하고 가자
//		for (int i = 0; i < arr.length; i++) {
//			if (i % 10 == 0) System.out.println();
//			System.out.print(arr[i] + "\t");
//		}
//		System.out.println();
		
		return arr; 
	}
	

}
