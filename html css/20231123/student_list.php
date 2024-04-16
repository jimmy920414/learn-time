<?php
$host = 'localhost';
$dbName = 'db_course';
$user = 'root';
$pass = '';
$dsn = "mysql:host=" . $host . ";dbname=" . $dbName;

try {
    $pdo = new PDO($dsn, $user, $pass);
    $query = "SELECT * FROM students";
    $stmt = $pdo->query($query);

    if ($stmt->rowCount() > 0) {
        echo '<table>'
            . '<tr>'
            . '<td>學號</td><td>姓名</td>'
            . '<td>電話</td><td>班級</td>'
            . '</tr>';

        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo '<tr>';
            echo '<td>' . $row['student_id'] . '</td>';
            echo '<td>' . $row['std_name'] . '</td>';
            echo '<td>' . $row['phone'] . '</td>';
            echo '<td>' . $row['class_name'] . '</td>';
            echo '</tr>';
        }

        echo '</table>';
    } else {
        echo "沒有符合條件的記錄。";
    }
} catch (PDOException $e) {
    echo '發生錯誤： ' . $e->getMessage();
}
?>
