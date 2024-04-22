package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.sound.midi.Soundbank;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw08 frame = new MySw08();
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
	public MySw08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 232, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(12, 10, 187, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		// 효율적으로 고쳐보자
//		btn1.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				tf.setText(tf.getText() + "1");
//				
//				System.out.println(e);
//				System.out.println(e.getSource());
//				System.out.println(e.getComponent());
//				JButton b = (JButton)e.getSource();
//				System.out.println(b.getText());
//				myClick(e);
//			}
//		});
		btn1.setBounds(12, 51, 46, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.setBounds(84, 51, 46, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.setBounds(153, 51, 46, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.setBounds(12, 95, 46, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.setBounds(84, 95, 46, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setBounds(153, 95, 46, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.setBounds(12, 141, 46, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.setBounds(84, 141, 46, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.setBounds(153, 141, 46, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		
		btn0.setBounds(12, 182, 46, 23);
		contentPane.add(btn0);
		
		JButton btn_call = new JButton("☎");
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myCall();
			}
		});
		btn_call.setBounds(84, 182, 115, 23);
		contentPane.add(btn_call);
		
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myClick(e); } });
		
	}
	
	void myCall() {
		tf.setHorizontalAlignment(JLabel.RIGHT);
		JOptionPane.showMessageDialog(null, "calling\n" + tf.getText(), "calling", JOptionPane.PLAIN_MESSAGE);
	}
	
	void myClick(MouseEvent e) {
		JButton b = (JButton)e.getSource();
		String str_new = b.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old + str_new);
	}

}


