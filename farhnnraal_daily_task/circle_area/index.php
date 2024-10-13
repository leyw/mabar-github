<!-- // Suggested code may be subject to a license. Learn more: ~LicenseLog:297887006. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circle Area Calculator</title>
</head>
<body>
    <h3>Program Menghitung Luas Lingkaran</h3>
    <form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="post">
        <laber type="number" for="jari-jari">Berapa Jari-jarinya?</laber>
        <br>
        <input type="number" name="jarijari">
        <br>
        <button type="submit">Hitung Sekarang!</button>
    </form>

    <?php

        // $jari_jari = isset($_POST['jarijari']) ? $_POST['jarijari'] : 0;
        $luas = 3.14 * pow(isset($_POST['jarijari']) ? $_POST['jarijari'] : 0, 2);
        echo "Luas lingkarannya: $luas";

    ?>
</body>
</html>