<!DOCTYPE html>
<html>

<head>
    <title>BMI計算資料</title>
    <meta charset="utf-8">
    <style>
        input[type="number"] {
            text-align: right;
        }
    </style>
</head>

<body>
    <form action="bmi_result.php" method="post">
        <?php
        echo '2411032029燕韋宏';
        ?>
        <div>
            身高：
            <?php
                echo $_POST['height'].'公分';
            ?>
        </div>
        <div>
            體重：
            <?php
                echo $_POST['weight'].'公斤';
            ?>
        </div>
        <?php
            $height = floatval($_POST['height'])/100;    
            $weight = floatval($_POST['weight']);    
            $total = $weight/($height*$height);
            echo '您的BMI為';
            echo round($total,1);
        ?>
        <?php
        if($total<18.5){
            echo'體重過輕';
        }
        else if($total < 24){
            echo '體重正常';
        }
        else if($total < 27){
            echo'體重過重';
        }
        else{
            echo'肥胖';
        }




        ?>
        <div>
            <input type="submit" value="送出" />
        </div>
    </form>
</body>

</html>