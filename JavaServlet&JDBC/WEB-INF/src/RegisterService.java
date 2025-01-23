import java.sql.*;

public class RegisterService {

        public boolean userExists ( String username ){
        
            User user = new DAO().select(username); 
            return user!=null;
        
    }

    public void createUser( User user ){
        new DAO().insertUser(user.getUsername(),user.getPassword());

    }


    
}