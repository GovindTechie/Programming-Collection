<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Page</title>
</head>
<body>
    <h1 align="center">Welcome to the registeration page</h1>
    <div align="center">
        <h1>
            <% 
                Object value=request.getAttribute("user_exists");
                if (value==null){
                    out.println("Welcome to registeration page");
                } else {
                    out.println(String.format( "Username '%s' is not available ",(String)value ));
                }
            %>
                    
        </h1>
    <form action="/lms/register" method="get" >
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
</body>
</html>