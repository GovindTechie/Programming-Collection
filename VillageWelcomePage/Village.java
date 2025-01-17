import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Village extends JFrame implements ActionListener {
    
    private JTextField visitorName = new JTextField(20);
    private JTextField visitorEmail = new JTextField(20);
    private JPasswordField password = new JPasswordField(20);
    private JButton login = new JButton("Login");
    private JButton newUser = new JButton("New User");

    public Village() {
        initComponents();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == login) {
            JOptionPane.showMessageDialog(this, "You have Successfully Logged In");
        } else if (e.getSource() == newUser) {
            JOptionPane.showMessageDialog(this, "Your data has been saved successfully");
        }
    }

    public void initComponents() {
        this.setTitle("Village Login");
        this.setLayout(new GridLayout(4, 2, 10, 10));
        this.setSize(400, 200);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        this.add(new JLabel("Name:"));
        this.add(visitorName);
        this.add(new JLabel("Email:"));
        this.add(visitorEmail);
        this.add(new JLabel("Password:"));
        this.add(password);
        this.add(login);
        this.add(newUser);

        login.addActionListener(this);
        newUser.addActionListener(this);
    }

}
