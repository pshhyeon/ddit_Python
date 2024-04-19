package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw02 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw02 frame = new MySw02();
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
	public MySw02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setText("100");
		tf.setBounds(39, 10, 65, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("INCREASE");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
//				tf.setText("" + (Integer.parseInt(tf.getText())  + 1));
			}
		});
		btn.setBounds(116, 9, 97, 23);
		contentPane.add(btn);
	}
	
	void myClick() {
		String tf_text =  tf.getText();
		int tf_num = Integer.parseInt(tf_text);
		tf_num ++;
		tf.setText(String.valueOf(tf_num));
	}
}
