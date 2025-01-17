public class RegistarationService {
    public void register(String username, String password) {
        DataAccessObject dao;
        dao = new DatabaseDAO();
        dao.save(username, password);
    }
}