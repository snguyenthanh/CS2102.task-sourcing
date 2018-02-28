import time

CONTENT1 = r"""
<html>
<head>
<title>Taskrr</title>
<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<link href="http://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">

<link rel="stylesheet" type="text/css" href="style.css">
<style>
body {
background: url(https://source.unsplash.com/GANqCr1BRTU/800x600);
background-size: cover;
background-position: center;
}

body,
html {
width: 100%;
height: 100%;
font-family: "Lato";
color: white;
}

h1 {
font-weight: 700;
font-size: 5em;
}


.content{
padding-top: 25%;
text-align: center;
text-shadow: 0px 4px 3px rgba(0,0,0,0.4),
             0px 8px 13px rgba(0,0,0,0.1),
             0px 18px 23px rgba(0,0,0,0.1);
}

hr {
width: 400px;
border-top: 1px solid #f8f8f8;
border-bottom: 1px solid rgba(0,0,0,0.2);
}
</style>
</head>

<body>

<!-- if you want a navbar -->
<nav class="navbar navbar-default navbar-fixed-top">
<div class="container">
<div class="navbar-header">
  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
    <span class="sr-only">Toggle navigation</span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
  </button>
  <a class="navbar-brand" href="#">Purrfect Match</a>
</div>
<div id="navbar" class="collapse navbar-collapse">
  <ul class="nav navbar-nav">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="contact">Contact</a></li>
  </ul>
  <ul class="nav navbar-nav navbar-right">
    <li><a href="/">Signup  <i class="fa fa-user-plus"></i></a></li>
    <li><a href="/about">Login  <i class="fa fa-user"></i></a></li>
  </ul>
</div>
</div>
</nav>

<div class="container">
<div class="row">
    <div class="col-lg-12">
        <div class="content">
            <h1>Taskrr</h1>
            <h3>Get things done.</h3>
            <hr>
            <button class="btn btn-default btn-lg">Get Started!</button>
        </div>
    </div>
</div>
</div>

</body>
</html>
"""

CONTENT2 = "<h1>This is a test</h1>"
