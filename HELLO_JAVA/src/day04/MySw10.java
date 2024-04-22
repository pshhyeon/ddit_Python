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
import java.util.Iterator;

public class MySw10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw10 frame = new MySw10();
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
	public MySw10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 290, 369);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("시작 별 수");
		lbl_first.setBounds(34, 10, 65, 30);
		contentPane.add(lbl_first);
		
		tf_first = new JTextField();
		tf_first.setBounds(123, 15, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		JLabel lbl_last = new JLabel("끝 별 수");
		lbl_last.setBounds(34, 53, 65, 30);
		contentPane.add(lbl_last);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(123, 58, 116, 21);
		contentPane.add(tf_last);
		
		JButton btnNewButton = new JButton("별 출력하기");
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btnNewButton.setBounds(34, 93, 205, 23);
		contentPane.add(btnNewButton);
		
		ta = new JTextArea();
		ta.setBounds(34, 139, 205, 152);
		contentPane.add(ta);
	}

	void myClick() {
		int first_num = Integer.parseInt(tf_first.getText());
		int last_num = Integer.parseInt(tf_last.getText());
		String str = "";
		
		for (int i = first_num; i <= last_num; i++) {
			for (int j = 0; j < i; j++) {
				str += "★";
			}
			str += "\n";
		}
		
		ta.setText(str);
	}
}
