$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {                                        //Here this is screen size
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {                                      //Here this is screen size
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {                                     //Here this is screen size
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})




var dropdowns = document.querySelectorAll('.dropdown');
for (var i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener('mouseenter', function() {
        this.querySelector('.dropdown-menu').style.display = 'block';
    });
    dropdowns[i].addEventListener('mouseleave', function() {
        this.querySelector('.dropdown-menu').style.display = 'none';
    });
}


