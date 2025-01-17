import java.io.*;

public class FileDAO implements DataAccessObject{
    public void save(String username, String password) {

        try {
            String fileName = "users.txt";
            FileWriter writer = new FileWriter(fileName, true);
            try {
                String data = String.format("%s, %s\n", username, password);
                writer.write(data);
            }
            finally {
                writer.close();
            }
        }
        catch (Exception ex){
            ex.printStackTrace();
            
        }

    }
}






