<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to Home</h1>
        <h1>
            <% 
                // Retrieving the "username" attribute from the request
                String user = (String) request.getAttribute("username"); 
                // Since getAttribute returns an object, it is typecasted to a String.
                out.println(user);
            %>
        </h1>
    </body>
</html>
