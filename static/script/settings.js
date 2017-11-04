$(document).ready(function () {

        $('.menu').click(function() {
            $('.overlay').toggleClass('anim');
        });

        $('.animation').click(function(){
            $('.anim').toggleClass('reverse-animation');
        })
});
