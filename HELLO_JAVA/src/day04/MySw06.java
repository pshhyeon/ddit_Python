package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw06 frame = new MySw06();
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
	public MySw06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 273, 411);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(127, 10, 94, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JLabel lbl = new JLabel("출력 단수 : ");
		lbl.setBounds(36, 13, 79, 15);
		contentPane.add(lbl);
		
		
		JTextArea ta = new JTextArea();
		ta.setBounds(36, 74, 185, 263);
		contentPane.add(ta);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				ta.setText(myClick());
			}
		});
		btn.setBounds(36, 41, 185, 23);
		contentPane.add(btn);
	}
	
	String myClick() {
		String tf_text = tf.getText();
		int tf_num = Integer.parseInt(tf_text);
		String dan = "";
		for (int i = 1; i < 9; i++) {
			dan += tf_num + " * " + i + " = " + (tf_num * i) + "\n"; 
		}
				
		return dan;
	}
	
}
