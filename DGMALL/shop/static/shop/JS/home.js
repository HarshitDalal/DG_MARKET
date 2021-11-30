var swiper = new Swiper('.swiper-container', {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 1500,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});
  
const productBox = document.querySelectorAll('.product-box');
productBox.forEach((list,index) =>{
    const discountPrice = list.querySelector('.discountprice');
    const realPrice = list.querySelector('.realprice');
    if (discountPrice.innerText.length>1) {
        realPrice.setAttribute('style','display: none;');
    }
});