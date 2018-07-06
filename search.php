PHP

<?PHP 
    include_once("connection.php"); 
    if( isset($_POST['txtbool']) ) { 
        $bool = $_POST['txtbool'];
        
        $query = "SELECT feature1 FROM data ". 
        " WHERE bool = '$bool'"; 
        
        $result = mysqli_query($conn, $query);
        
        if($result->num_rows > 0){
            
                echo "success"; 
                exit; 
            
          //  header("location: main.html"); //replace index.php with your url
        } else{ 
            echo "No data <br/>"; 
        } 
    } 
?>
<html>
<head><title>Login|KosalGeek</title></head>
    <body>
        <h1>Login Example|<a href=”http://www.kosalgeek.com”>KosalGeek</a></h1>
        <form action="<?PHP $_PHP_SELF ?>" method="post">
            Bool: <input type="text" name="txtbool" value="" /><br/>
            <input type="submit" name="btnSubmit" value="Login"/>
        </form>
    </body>
</html>
