<?php
    if(isset($_POST['LogIn']))
    {
        $email=$_POST['Email_phone'];
        $pass=$_POST['Password'];
		echo "You have entered email::  ".$email;
		echo nl2br("\n");
        echo "You have entered password::  ".$pass;
    }
    else if(isset($_POST['submit']))
    {
        $first=$_POST['firstname'];
        $last=$_POST['surname'];
        $email=$_POST['emaill'];
        $pass=$_POST['passw'];
        echo "You have entered First Name::  ".$first;
		echo nl2br("\n");
        echo "You have entered Last Name::  ".$last;
        echo nl2br("\n");
        echo "You have entered email::  ".$email;
		echo nl2br("\n");
        echo "You have entered password::  ".$pass;
    }
?>