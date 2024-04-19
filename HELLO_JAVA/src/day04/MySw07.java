package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_me;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw07 frame = new MySw07();
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
	public MySw07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 262, 387);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl01 = new JLabel("나");
		lbl01.setBounds(24, 21, 57, 15);
		contentPane.add(lbl01);
		
		JLabel lbl02 = new JLabel("컴");
		lbl02.setBounds(24, 71, 57, 15);
		contentPane.add(lbl02);
		
		JLabel lbl03 = new JLabel("결과");
		lbl03.setBounds(24, 120, 57, 15);
		contentPane.add(lbl03);
		
		tf_me = new JTextField();
		tf_me.setBounds(96, 18, 116, 21);
		contentPane.add(tf_me);
		tf_me.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(96, 68, 116, 21);
		contentPane.add(tf_com);
		
		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(93, 117, 116, 21);
		contentPane.add(tf_result);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(12, 171, 200, 23);
		contentPane.add(btn);
	}
	
	void myClick() {
		String tf_me_text = tf_me.getText();
		if (tf_me_text != null && !tf_me_text.isEmpty()) {
			if(Math.random() < 0.5) {
				tf_com.setText("짝");
			} else {
				tf_com.setText("홀");
			} 
			
			if (tf_me_text.equals(tf_com.getText())) {
				tf_result.setText("정답");
			} else {
				tf_result.setText("오답");
			}
		} else {
			tf_result.setText("홀 or 짝을 입력");
		}
	}

}
