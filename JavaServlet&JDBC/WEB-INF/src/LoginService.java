public class LoginService {
    public boolean validate(User user){
        User validUser=new DAO().select(user.getUsername(),user.getPassword());
        return validUser!=null;
    }
}