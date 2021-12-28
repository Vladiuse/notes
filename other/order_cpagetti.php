<?php 
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	$uri = 'http://api.cpagetti.com/order/register';

    $order = [
        'api_key' => 'xxxxxxxxxxxxxxxx', // ваш API ключ
        'name' => $_REQUEST['name'],
        'phone' => $_REQUEST['phone'],
        'offer_id' => 'XXXX', //  ID оффера
       'country' => 'XX',  // страна https://ru.wikipedia.org/wiki/ISO_3166-1
		'lang' => 'XX', // язык https://www.exlab.net/tools/tables/languages.html
		'stream_code' => 'XXXX',  // айди потока (необязательно)
		'ip' => (!empty($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : null),
        'sub1' => $_REQUEST['sub1'], 
        'sub2' => $_REQUEST['sub2'], 
        'sub3' => $_REQUEST['sub3'],
        'sub4' => $_REQUEST['sub4'],
    ];
	
$headers = [
    "Host" => $uri,
    "User-Agent" => (!empty($_SERVER['HTTP_USER_AGENT']) ? $_SERVER['HTTP_USER_AGENT'] : null),
    "Accept" => (!empty($_SERVER['HTTP_ACCEPT']) ? $_SERVER['HTTP_ACCEPT'] : null),
    "Accept-Language" => (!empty($_SERVER['HTTP_ACCEPT_LANGUAGE']) ? $_SERVER['HTTP_ACCEPT_LANGUAGE'] : null),
    "Keep-Alive" => '15',
    "Connection" => "keep-alive",
    "Referer" => (!empty($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : null),
];

$curl = curl_init();

curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
curl_setopt($curl, CURLOPT_URL, $uri);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_POSTFIELDS, $order);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$return= curl_exec($curl); 
curl_close($curl); 
// ЗАПИСЬ В LOG.TXT
// name; phone; date; ip
// {server_answer}
$today = date("m.d.y H:i:s");
$ip = (!empty($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : null);

$message = $_POST['name'] . ";" . $_POST['phone'] . ";" . $today . ";" .$ip . "\n";
file_put_contents('log.txt', $message, FILE_APPEND | LOCK_EX);
file_put_contents('log.txt', $return . "\n", FILE_APPEND | LOCK_EX);
}
 header('Location: success/success.html', true, 302);
    exit;
	
?>