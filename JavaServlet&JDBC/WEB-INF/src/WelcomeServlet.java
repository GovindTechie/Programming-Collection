import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class WelcomeServlet extends HttpServlet {

    public void doGet ( HttpServletRequest request , HttpServletResponse response ) throws ServletException , IOException {

        response.sendRedirect("jsp/login.jsp");

    }
}
