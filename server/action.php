<?php

$action = $_POST['action']; //What we are being polled for.
$coord = $_POST['coords'];

if(isset($action)) { 
  switch ($action) {
    case "connect":
        //Request connection
        break;
    case "hit":
        if(isset($coord)) {
          // Play has chosen hit here
        }else{
          // Invalid coord
        }
        break
    default:
  } 
}else{
  echo "ERROR: No action specified";
}
?>
