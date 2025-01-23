import java.net.URL;
import java.sql.*;

public class DAO {
    private Connection con;  //instance variable

    //if final var is a local variable then it has to be inititalized in the line of declaration itself 
    private static final String DRIVER;
    private static final String URL;
    private static final String USERNAME;
    private static final String PASSWORD;
    
    static{
        DRIVER = "com.mysql.cj.jdbc.Driver";
        URL = "jdbc:mysql://localhost:3306/lms";
        USERNAME="root";
        PASSWORD="abc123";
    }


    //non static blocks are called before constructors - represented by {}

    static {
        try {
            Class.forName( DRIVER );
        } catch ( ClassNotFoundException ex ){
            ex.printStackTrace();
        }
    }

    //constructor for DAO
    public DAO(){
        //create connection
        try {
            con = DriverManager.getConnection( URL, USERNAME, PASSWORD );
        } catch ( SQLException ex ){
            ex.printStackTrace();
        }
    }

    public void insertUser( String username , String password )  {
        //create and run the query
        //close the conection
        try { 
            try {
                String query = "insert into users(username,password) values(?,?)";
                PreparedStatement ps = con.prepareStatement(query);
                ps.setString(1, username);
                ps.setString(2, password);
                ps.executeUpdate(); 
            } finally {
                con.close();
            }
        } catch (SQLException ex){
            ex.printStackTrace();
            
        } 
        //this design is used for file handling too , as it is efficient rather than using try and catch blocks in finally.
    }
            
    public User select( String username ) {
        try {
            try{
                 String query = "select * from users where username=?";
                PreparedStatement ps=con.prepareStatement(query);
                ps.setString(1, username);
                ResultSet rs = ps.executeQuery();
                if (rs.next()){
                    String user = rs.getString("username");
                    String pass = rs.getString("password");
                    return new User(username,pass);
                    

                
                }
            } finally{
                con.close();
            }
        } catch (SQLException ex){
            ex.printStackTrace();
             
        }
        return null;
        
    }
 

    
    public User select( String username , String password ) {
        //create and run the query
        //close the conection
        try{
            try{
                String query = " select * from users where username=? and password=?";
                PreparedStatement ps = con.prepareStatement(query);
                ps.setString(1, username);
                ps.setString(2, password);
                ResultSet rs = ps.executeQuery(); //executeQuery returns an object of ResultSet
                if (rs.next()){
                   String user = rs.getString("username");
                   String pass=rs.getString("password");
                   return new User (user,pass);
                } 
            } finally {
                con.close();
            }
        }catch (SQLException ex){
            ex.printStackTrace();
        }
        return null;
        
    }
}

