import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class RegisterServlet extends HttpServlet  {
    public void doGet ( HttpServletRequest request , HttpServletResponse response) throws ServletException ,  IOException {

        String username=request.getParameter("username");
        String password=request.getParameter("password");

        //Registration servlet acts as a service layer and will forward the data to DAO layer

        // new DAO().add(username, password);

        //check if user exists (RegisterService)
        //if yes : register.jsp (username taken)
        //if not : RegisterService (create user)

        RegisterService service = new RegisterService();

        if (service.userExists(username)) {
            request.setAttribute("user_exists" , username);
            request.getRequestDispatcher("jsp/register.jsp").forward(request,response);
        } else {
            service.createUser(new User(username,password));
            request.setAttribute("user_created","");
            request.getRequestDispatcher("jsp/login.jsp").forward(request,response);
        }



    }
}