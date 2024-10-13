<?php

    session_start();

    if ( isset($_POST['logout']) )
    {
        session_unset();

        session_destroy();

        header('Location: ');
    }

    if ( !isset($_SESSION['status']) && $_SESSION['status'] != "session_approved" )
    {
        header('Location: ./login/');
    }

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circle Area Calculator</title>
</head>
<body>
    <form action="" method="post">
        <button type="submit" name="logout">Logout</button>
    </form>

    <br>

    <h3>Program Menghitung Luas Lingkaran</h3>
    <form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="post">
        <laber type="number" for="jari-jari">Berapa Jari-jarinya?</laber>
        <br>
        <input type="number" name="jarijari">
        <br>
        <button type="submit">Hitung Sekarang!</button>
    </form>
</body>
</html>

<?php

    function countArea( $jari_jari )
    {
        $luas = 3.14 * pow($jari_jari, 2);
        echo "Luas lingkarannya dari jari-jari = $jari_jari adalah: $luas";
    }

    $jari_jari = isset($_POST['jarijari']) ? $_POST['jarijari'] : 0;

    if ($jari_jari != NULL)
    {
        countArea( $jari_jari );    
    } else
    {
        echo "Angka nya mana le?";
    }

    if (isset($_POST['jarijari'])) {
        $jariJari = $_POST['jarijari'];
        $luas = pi() * pow($jariJari, 2);
        echo "Luas lingkaran dengan jari-jari $jariJari adalah: $luas";
    } else {
        echo "Masukkan jari-jari lingkaran!";
    }