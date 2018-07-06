<?php
$servername = "localhost"; //replace it with your database server name
$username = "id4837814_root";  //replace it with your database username
$password = "1234567890";  //replace it with your database password
$dbname = "id4837814_info";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>