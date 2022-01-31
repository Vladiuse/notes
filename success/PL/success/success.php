
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
  <meta lang="pl">
  <title>
  Dziękuję!
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
        <h2><span>Dziękujemy!</span> Twoje zamówienie zostało otrzymane!
           </h2>
           <p>Nasz operator skontaktuje się z Tobą w celu potwierdzenia zamówienia.
             <br>Dostawa realizowana jest kurierem lub pocztą. Płatność przy odbiorze!
           </p>
        </div>
        <div class="data">
          <h2><span>Dane aplikacji</span></h2>
          <p>Imię:<span class="userName"><?php echo $name;?></span></p>
          <p>Telefon: <span class="userPhone"><?php echo $phone;?></span></p>

          <p class="error"><span style="color: red;">*</span>jeśli popełniłeś błąd<br> - wyślij zgłoszenie ponownie.</p>
          <button onclick="showForm()" class="edit" id="fix">Poprawić</button>
          <form id="again-form" class="reForm" action="../order.php" method="POST">
            <input class="reName" name="name" placeholder="Twoje imię:" maxlength="30" value="<?php echo $name;?>"><br>
            <input class="rePhone" name="phone" placeholder="Twój numer telefonu:" minlength="8" maxlength="30" value="<?php echo $phone;?>"><br>
            <button type="submit" class="edit send">Wysłać</button>
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
