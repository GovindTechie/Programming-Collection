<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <div align="center">
        <h1>Login Page</h1>
        <h1>
            <%
                if (request.getAttribute("user_created") != null){
                    out.println("Account successfully created");
                }else if(request.getAttribute("invalid_credentials")!=null){
                    out.println("Invalid Crediantials");
                } else {
                    out.println("Welcome to login page");
                }
            %>
        </h1>
        <br />



    <form action="/lms/login" method="get" >
        <table>
            <tr>
                <th>Username</th>
                <td><input type="text" name="username"></td>
            </tr>
            <tr>
                <th>Password</th>
                <td><input type="password" name="password"></td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td><input type="submit"></td>
            </tr>
        </table>
    </form>
    </div>

    <div align="center">
        <a href="register.jsp">Create a new account</a>

    </div>



</body>
</html>