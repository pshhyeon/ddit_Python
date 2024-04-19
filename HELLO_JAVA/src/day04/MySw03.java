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

public class MySw03 extends JFrame {

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
					MySw03 frame = new MySw03();
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
	public MySw03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		tf01 = new JTextField();
		tf01.setBounds(44, 10, 85, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);

		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(160, 10, 85, 21);
		contentPane.add(tf02);

		tf03 = new JTextField();
		tf03.setColumns(10);
		tf03.setBounds(315, 10, 85, 21);
		contentPane.add(tf03);

		JLabel lbl = new JLabel("X");
		lbl.setBounds(141, 13, 19, 15);
		contentPane.add(lbl);

		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(251, 9, 52, 23);
		contentPane.add(btn);
	}

	void myClick() {
		String tf01_text = tf01.getText();
		String tf02_text = tf02.getText();
		int tf01_num = Integer.parseInt(tf01_text);
		int tf02_num = Integer.parseInt(tf02_text);
		int tf03_num = tf01_num * tf02_num;
		tf03.setText(String.valueOf(tf03_num));
	}
}
