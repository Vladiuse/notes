<?php
// ЗАПИСЬ В LOG.TXT
$today = date("m.d.y H:i:s");
$message = $_POST['name'] . ";" . $_POST['phone'] . ";" . $today . ";" . $response['status'] . "\n";
file_put_contents('log.txt', $message, FILE_APPEND | LOCK_EX);
?>