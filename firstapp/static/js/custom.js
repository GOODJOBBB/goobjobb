$(document).ready(function(){
    $('#main').each(function(){
        $(window).resize(function(){
            // var winWidth=$(window).width();
            var boxWidth=$('.box').width();

            $('.box').height(boxWidth*0.681);
            
            // if(winWidth<=1920){
            //     $('.box').height(boxWidth*0.681);
            // }
        });

    });

});