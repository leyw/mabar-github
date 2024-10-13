<?php

    session_start();

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Login Document</title>
</head>
<body>
    <div class="container p-3">
        <h1>Login</h1>
        
        <form method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">

            <div class="row align-items-center p-2">
                <div class="col">
                    <input class="form-control" type="text" id="username" name="username" placeholder="Username" aria-label="Username" aria-describedby="usernameHelp" required>
                </div>

                <div id="usernameHelp" class="form-text col">
                    <span>Forgot Username?</span>
                </div>
            </div>
            
            <div class="row align-items-center p-2">
                <div class="col">
                    <input class="form-control" type="password" id="password" name="password" placeholder="Password" aria-label="Password" aria-describedby="passwordHelp" required>
                </div>

                <div id="passwordHelp" class="form-text col">
                    <span>Forgot Password?</span>
                </div>
            </div>
    
            <div class="row-auto align-items-center p-2">
                <button class="btn btn-primary" type="submit">Login</button>
            </div>
    
        </form>
    </div>

</body>
</html>    

    $account = [
        "username" => "hello",
        "password" => "hi"
    ];

    if (isset($_POST['username']) && isset($_POST['password'])) {
        if ($_POST['username'] === $account['username'] && $_POST['password'] === $account['password']) {
            $_SESSION['status'] = 'session_approved';
            header('Location: ../');
        } else {
            echo 'Login failed!';
        }
    }
