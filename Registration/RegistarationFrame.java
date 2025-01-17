import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


public class RegistarationFrame extends JFrame implements ActionListener{
    private JTextField usernameField;
    private JTextField passwordFiled;
    private JButton registorButton;

    public RegistarationFrame () {
        this.initComponents();
    }

    public void actionPerformed(ActionEvent event){
        String username = usernameField.getText();
        String password = passwordFiled.getText();
        RegistarationService service = new RegistarationService();
        service.register(username, password);
    }
    
    private void initComponents () {
        usernameField = new JTextField(20);
        passwordFiled = new JPasswordField(20);
        registorButton = new JButton("Resister");
        registorButton.addActionListener(this);

        this.setLayout(new FlowLayout());

        this.add(usernameField);
        this.add(passwordFiled);
        this.add(registorButton);

        this.setSize(500,300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

}
