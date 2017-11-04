var myDate = new Date();
  /* Uur voor de middag */
if ( myDate.getHours() < 12 )
{
    document.write('<h1 class="aanspreking">'+'Goedemorgen'+'</h1>');
}
else  /* Uur van middag tot 16.59 */
if ( myDate.getHours() >= 12 && myDate.getHours() <= 17 )
{
    document.write('<h1 class="aanspreking">'+'Goedenamiddag'+'</h1>');
}
else  /*Het uur is na 17 uur tussen 18 en middernacht */
if ( myDate.getHours() > 17 && myDate.getHours() <= 24 )
{
    document.write('<h1 class="aanspreking">'+'Goedenavond'+'</h1>');
}

else  /* Het uur is niet tussen 0 en 24 uur */
{
    document.write('<h1 class="aanspreking">'+'Goeiedag'+'</h1>');
}


