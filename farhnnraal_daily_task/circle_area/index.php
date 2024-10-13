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

    ?>
</body>
</html>