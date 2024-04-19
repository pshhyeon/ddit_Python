package day04;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySw01 extends JFrame{

	private JPanel contentPane;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySw01 frame = new MySw01();
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
	public MySw01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("Good Morning");
		lbl.setBounds(66, 27, 109, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("CLICK");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				System.out.println("btn_click");
				lbl.setText("Good Evening"); 
			}
		});
		btn.setBounds(206, 23, 97, 23);
		
		// ActionListener 등록
//		btn.addActionListener(this);
		
		contentPane.add(btn);
	}
	// action implement해야함
//    @Override
//    public void actionPerformed(ActionEvent e) {
//        lbl.setText("Good Evening"); 
//    }
	

}

