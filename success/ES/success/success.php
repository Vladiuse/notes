
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
  <meta lang="es">
  <title>
  ¡Gracias!
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
          <h2><span>¡Gracias!</span> ¡Tu pedido es aceptado!
          </h2>
          <p>Nuestro operador se pondrá en contacto contigo para confirmar el pedido.
            <br>La entrega se realiza por mensajería o correo. ¡Pago a la entrega!
          </p>
        </div>
        <div class="data">
          <h2><span>Datos de la aplicación</span></h2>
          <p>Nombre: <span class="userName"><?php echo $name;?></span></p>
          <p>Teléfono: <span class="userPhone"><?php echo $phone;?></span></p>

          <p class="error"><span style="color: red;">*</span>si cometes un error<br> - envíe su solicitud de nuevo.</p>
          <button onclick="showForm()" class="edit" id="fix">Corregir</button>
          <form id="again-form" class="reForm" action="../order.php" method="POST">
            <input class="reName" name="name" placeholder="Tu nombre:" maxlength="30" value="<?php echo $name;?>"><br>
            <input class="rePhone" name="phone" placeholder="Su número de teléfono:" minlength="8" maxlength="30" value="<?php echo $phone;?>"><br>
            <button type="submit" class="edit send">Enviar</button>
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

