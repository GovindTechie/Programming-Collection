import java.sql.*;

public class DatabaseDAO implements DataAccessObject{
    public void save(String username, String password) {
        try {
            // 1. laod the driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            System.out.println("Connected to Driver");

            // 2. create connnection
            String url = "jdbc:mysql://localhost:3306/school";
            String user = "root";
            String pass = "Khedkar@123m";
            Connection con;
            con = DriverManager.getConnection(url, user, pass);

            System.out.println("Connected to DB");

            // 3. create and run the query
            String query = "insert into student(student_name, password) values(?, ?)";
            PreparedStatement ps = con.prepareStatement(query);
            ps.setString(1, username);
            ps.setString(2, password);
            ps.executeUpdate();

            // 4. close connection
            con.close();


        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
