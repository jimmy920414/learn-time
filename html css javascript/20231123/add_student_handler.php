    <?php
    $stdName = $_POST['std_name'];
    $phone = $_POST['phone'];
    $className = $_POST['class_name'];

    $sql = "INSERT INTO students (std_name, phone, class_name) VALUES (:stdName, :phone, :className)";
    $host = 'localhost';
    $dbName = 'db_course';
    $user = 'root';
    $pass = '';
    $dsn = "mysql:host=" . $host . ";dbname=" . $dbName;

    try {
        $pdo = new PDO($dsn, $user, $pass);
        $query = $pdo->prepare($sql);
        $query->bindParam(':stdName', $stdName);
        $query->bindParam(':phone', $phone);
        $query->bindParam(':className', $className);
        $query->execute();
        echo '新增完成。<a href="student_list.php">學生列表</a>';
    } catch (PDOException $e) {
        echo '發生錯誤：' . $e->getMessage();
    }
    ?>
