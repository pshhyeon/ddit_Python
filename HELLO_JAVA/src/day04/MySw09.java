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

public class MySw09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	private int com = (int)(Math.random() * 99 ) + 1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw09 frame = new MySw09();
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
	public MySw09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 245, 285);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞출 수");
		lbl.setBounds(12, 10, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(101, 7, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("숫자 맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(12, 43, 205, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(12, 76, 205, 120);
		contentPane.add(ta);
	}
	
	void myClick() {
//		System.out.println(com);
		int mine = Integer.parseInt(tf.getText());
		String ta_text = ta.getText();
		if(mine > com) {
			ta.setText(ta_text + mine + " DW\n");
		} else if (mine < com){
			ta.setText(ta_text + mine + " UP\n");
		} else {
			ta.setText(ta_text + mine + " 정답\n");
		}
		tf.setText("");
	}
	
}
