<!DOCTYPE html>
<html>
<head>
    <title>Login</title>    
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">

        <h1>Login</h1>

        <form method="post" action="process_login.php">

            <class class="row-auto">
                <class class="col-auto">
                    <label class="form-label" for="username">Username:</label>
                </class>
            </class>

            <class class="row-auto">
                <class class="col-auto">
                    <input class="form-control" type="text" id="username" name="username" aria-describedby="usernameHelp" required>
                </class>
                <class class="col-auto">
                    <span id="usernameHelp" class="form-text">
                        <a href="#">Forgot username?</a>
                    </span>
                </class>
            </class>

            <class class="row-auto">
                <class class="col-auto">
                    <label class="form-label" for="password">Password:</label>
                </class>
            </class>

            <class class="row-auto">
                <class class="col-auto">
                    <label class="form-label" for="password">Password:</label>
                </class>
            </class>

            <class class="row-auto">
                <class class="col-auto">
                    <input class="form-control" type="password" id="password" name="password" aria-describedby="passwordHelp" required>
                </class>
                <class class="col-auto">
                    <span id="passwordHelp" class="form-text">
                        <a href="#">Forgot password?</a>
                    </span>
                </class>
            </class>
    
            <class class="row-auto">
                <class class="col-auto">
                    <button type="submit">Login</button>
                </class>
            </class>

        </form>
        
    </div>
</body>
</html>