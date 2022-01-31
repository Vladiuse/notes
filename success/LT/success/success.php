
<?php
if(isset($_GET['name'])) {
   $name = $_GET['name'];
}
if(isset($_GET['phone'])) {
   $phone = $_GET['phone'];
}
if(isset($_GET['fbp'])) {
  $fbp = $_GET['fbp'];
}
?>
<!DOCTYPE html>
<html>

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta lang="lt">
  <title>
    Ačiū
  </title>

  <meta name="viewport" content="width=320">
  <meta name="MobileOptimized" content="width=320">
  <link href="./success/css" rel="stylesheet" type="text/css">
  <link media="all" rel="stylesheet" type="text/css" href="order-style.css">

  <!-- Facebook Pixel Code -->
  <img height="1" width="1" src="https://www.facebook.com/tr?id=<?php echo $fbp;?>&ev=Lead&noscript=1" />
  <!-- End Facebook Pixel Code -->

</head>

<body>

  <div id="wrapper">
    <div class="container">
      <span class="decoration">
      </span>
      <div class="order-block">
        <div class="text-holder">
          <h2><span>Ačiū</span> Jūsų užsakymas priimtas!
          </h2>
          <p>Mūsų operatorius susisieks su jumis, kad patvirtintų užsakymą.
            <br>Pristatymas vykdomas per kurjerį arba paštu. Apmokėjimas pristatymo metu!
          </p>
        </div>
        <div class="data">
          <h2><span>Programos duomenys</span></h2>
          <p>Vardas: <span class="userName"></span></p>
          <p>Telefonas: <span class="userPhone"></span></p>

          <p class="error"><span style="color: red;">*</span>jei padarysi klaidą<br> - dar kartą pateikite paraišką.</p>
          <button onclick="showForm()" class="edit" id="fix">Pataisyti</button>
          <form id="again-form" class="reForm" action="../order.php" method="POST">
            <input class="reName" name="name" placeholder="Tavo vardas:" maxlength="30" value="<?php echo $name;?>"><br>
            <input class="rePhone" name="phone" placeholder="Jūsų telefono numeris:" minlength="8" maxlength="30" value="<?php echo $phone;?>"><br>
            <button type="submit" class="edit send">Siųsti</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  <script>
    function showForm() {
      var fixBtn = document.getElementById("fix");
      fixBtn.style.display = "none";
      var againFrom = document.getElementById("again-form");

      againFrom.classList.toggle('show')
    }

  </script>

</body>

</html>