<!DOCTYPE html>
<html>

<head>
    <title>門票費用</title>
    <meta charset="utf-8">
</head>

<body>
    <form action="ticket_price.php" method="post">
        <table>
            <tr>
                <td>全票 120元</td>
                <td>
                    <?php echo $_POST['full_fare'] . ' 張'; ?>
                </td>
            </tr>
            <tr>
                <td>半票 50元</td>
                <td>
                    <?php echo $_POST['half_fare'] . ' 張'; ?>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <?php
                    $full_fare = intval($_POST['full_fare']);
                    $half_fare = intval($_POST['half_fare']);
                    $total = $full_fare * 120 + $half_fare * 50;
                    echo '共 ' . $total . ' 元';
                    ?>
                </td>
            </tr>
        </table>
    </form>
</body>

</html>