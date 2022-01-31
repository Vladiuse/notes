
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
  <meta lang="pt">
  <title>
  Obrigado!
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
          <h2><span>Obrigado!</span> Seu pedido foi aceito!
          </h2>
          <p>Nosso operador entrará em contato com você para confirmar o pedido.
            <br>A entrega é feita por correio ou correio. Pagamento na entrega!
          </p>
        </div>
        <div class="data">
          <h2><span>Dados de aplicativos</span></h2>
          <p>Nome: <?php echo $name;?></p>
          <p>Telefone: +<?php echo $phone;?></p>

          <p class="error"><span style="color: red;">*</span>se você errou<br> - submeta a sua candidatura novamente.</p>
          <button onclick="showForm()" class="edit" id="fix">Corrigir</button>
          <form id="again-form" class="reForm" action="../order.php" method="POST">
            <input class="reName" name="name" placeholder="Seu nome:" maxlength="30" value="<?php echo $name;?>"><br>
            <input class="rePhone" name="phone" placeholder="Seu número de telefone:" minlength="8" maxlength="30" value="<?php echo $phone;?>"><br>
            <button type="submit" class="edit send">Mandar</button>
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