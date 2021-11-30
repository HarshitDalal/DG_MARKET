var swiper = new Swiper('.swiper-container', {
    effect: 'flip',
    grabCursor: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});