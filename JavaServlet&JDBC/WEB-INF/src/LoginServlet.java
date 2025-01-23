import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.*;
import javax.servlet.http.*;

public class LoginServlet extends HttpServlet {
    public void doGet( HttpServletRequest request, HttpServletResponse response ) throws ServletException,IOException {

        String username = request.getParameter("username");
        //username = raj (paramater)
        //username       (parameter name)
        //raj            (parameter value)
        
        String password = request.getParameter("password"); 

        // PrintWriter out = response.getWriter();
        // out.println("Welcome ," + username);


        // response.sendRedirect("jsp/home.jsp");
        
        User user = new User (username,password);
        LoginService service = new LoginService();
        if (service.validate(user)){
            request.setAttribute("username",username);
            RequestDispatcher dispatcher = request.getRequestDispatcher("jsp/home.jsp");
            dispatcher.forward(request,response);
        } else {
            request.setAttribute("invalid_credentials","");
            RequestDispatcher dispatcher = request.getRequestDispatcher("jsp/login.jsp");
            dispatcher.forward(request,response);
        }

        //using request and sending data
        
        
    }  
}