
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
  <meta lang="fr">
  <title>
  Merci!
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
        <h2><span>Merci !</span> Votre commande a été reçue !
           </h2>
           <p>Notre opérateur vous contactera pour confirmer la commande.
             <br>La livraison est effectuée par coursier ou par la poste. Paiement à la livraison!
           </p>
        </div>
        <div class="data">
          <h2><span>Application Data</span></h2>
          <p>Votre nom: <span class="userName"><?php echo $name;?></span></p>
          <p>Телефон: <span class="userPhone"><?php echo $phone;?></span></p>

          <p class="error"><span style="color: red;">*</span>si vous avez fait une erreur<br> - renvoyez la candidature.</p>
          <button onclick="showForm()" class="edit" id="fix">Corriger</button>
          <form id="again-form" class="reForm" action="../order.php" method="POST">
            <input class="reName" name="name" placeholder="Votre nom:" maxlength="30" value="<?php echo $name;?>"><br>
            <input class="rePhone" name="phone" placeholder="Téléphone:" minlength="8" maxlength="30" value="<?php echo $phone;?>"><br>
            <button type="submit" class="edit send">Envoyer</button>
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
