
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
  <meta lang="al">
  <title>
  Faleminderit!
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
          <h2><span>Faleminderit!</span> Porosia juaj është marrë!
           </h2>
           <p>Operatori ynë do t'ju kontaktojë për të konfirmuar porosinë.
             <br>Dorëzimi kryhet me korrier ose postë. Pagesa me dërgesë!
           </p>
        </div>
        <div class="data">
          <h2><span>Të dhënat e aplikacionit</span></h2>
          <p>Emri juaj: <span class="userName"><?php echo $name;?></span></p>
          <p>Numri juaj i telefonit:<span class="userPhone"><?php echo $phone;?></span></p>

          <p class="error"><span style="color: red;">*</span>nëse keni bërë një gabim<br> - dërgoni përsëri aplikacionin.</p>
          <button onclick="showForm()" class="edit" id="fix">Për të korrigjuar</button>
          <form id="again-form" class="reForm" action="../order.php" method="POST">
            <input class="reName" name="name" placeholder="Emri juaj:" maxlength="30" value="<?php echo $name;?>"><br>
            <input class="rePhone" name="phone" placeholder="Numri juaj i telefonit:" minlength="8" maxlength="30" value="<?php echo $phone;?>"><br>
            <button type="submit" class="edit send">dërgoni</button>
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
