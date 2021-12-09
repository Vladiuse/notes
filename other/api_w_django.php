<?php
if (empty( $_POST )) die("Bad request");
$data = $_POST;
$pp_name = 'tt';  # code PP Trirazat
$data["offer"] = 0;
$data["flow"] = 0;
$data["base"] = "0";
$data["currency"] = "EUR";
$data["country"] = '';
$data["comm"] = 'lt lv ee';
$data["ip"] = $_SERVER["HTTP_CF_CONNECTING_IP"] ? $_SERVER["HTTP_CF_CONNECTING_IP"] : ( $_SERVER["HTTP_X_FORWARDED_FOR"] ? $_SERVER["HTTP_X_FORWARDED_FOR"] : $_SERVER["REMOTE_ADDR"] );
$data["ua"] = $_SERVER["HTTP_USER_AGENT"];
if (isset( $data["phonecc"] )) $data["phone"] = $data["phonecc"].$data["phone"];
# Prepare Data
$to_django = $data;
$to_django['price'] = $to_django['base'];
$to_django['offer_id'] = $to_django['offer'];
$to_django['flow_id'] = $to_django['flow'];
$to_django['pp_name'] = $pp_name;
$domain_name = parse_url($_SERVER['SERVER_NAME']);
$to_django['domain'] = $domain_name['path'];
# ----------------
$data = http_build_query( $data );
$curl = curl_init( "https://my.trirazat.com/api/wm/push.json?id=35-9a9af61c8becb254297fdb13159b20d1" );
curl_setopt( $curl, CURLOPT_RETURNTRANSFER, true );
curl_setopt( $curl, CURLOPT_TIMEOUT, 30 );
curl_setopt( $curl, CURLOPT_POST, 1 );
curl_setopt( $curl, CURLOPT_POSTFIELDS, $data );
$result = json_decode( curl_exec( $curl ), true );
curl_close( $curl );
$today = date("m.d.y H:i:s");
$name = $_POST['name'];
$phone = $_POST['phone'];
$my_ip = $_SERVER["HTTP_CF_CONNECTING_IP"] ? $_SERVER["HTTP_CF_CONNECTING_IP"] : ( $_SERVER["HTTP_X_FORWARDED_FOR"] ? $_SERVER["HTTP_X_FORWARDED_FOR"] : $_SERVER["REMOTE_ADDR"] );
$message = "$today;$name;$phone;$my_ip\n";
file_put_contents('log.txt', $message, FILE_APPEND | LOCK_EX); 
# get id of lead from PP answer 
if ($result['status'] == 'ok'){
    $to_django['lead_id'] = $result['id'];
}
$to_django['pp_answer'] = json_encode($result);
# ----------------
if ( $result["url"] ) {
	header( "Location: " . $result["url"] );
} else header( "Location: /success/success.php?name=$name&phone=$phone&" . http_build_query($result) );

# send lead to Django 
$url = "https://main-prosale.store/api/add_lead/";
$fields_string = http_build_query($to_django);
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_POST, true);
curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
$django_result = curl_exec($ch);
#echo $django_result;
# ---------------- 
die();
?>

<?php
# вывести файлы текущей директории
$dir    = __DIR__;
$files1 = scandir($dir);
$res = '';
foreach ($files1 as $value) {
    if(stristr($value, '.') === FALSE) {
        $res = $res . $value . ';';
    }
  }

print($res);
die();
?>