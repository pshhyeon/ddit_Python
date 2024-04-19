package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;

public class MySw04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw04 frame = new MySw04();
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
	public MySw04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf01 = new JTextField();
		tf01.setBounds(22, 10, 58, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(140, 10, 58, 21);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		tf03.setColumns(10);
		tf03.setBounds(332, 10, 58, 21);
		contentPane.add(tf03);
		
		JLabel lbl = new JLabel("에서");
		lbl.setBounds(100, 13, 38, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("까지 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(220, 9, 97, 23);
		contentPane.add(btn);
	}
	
	void myClick() {
		String tf01_text = tf01.getText();
		String tf02_text = tf02.getText();
		int tf01_num = Integer.parseInt(tf01_text);
		int tf02_num = Integer.parseInt(tf02_text);
		int tf03_num = 0;
		for (int i = tf01_num; i <= tf02_num; i++) {
			tf03_num += i;
		}
		tf03.setText(String.valueOf(tf03_num));
	}

}
