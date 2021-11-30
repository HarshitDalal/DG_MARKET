var viewsByWidth = 0;
let responsive = [
    {breakpoint:{width:0,viewsByWidth:2}},
    {breakpoint:{width:768,viewsByWidth:2}},
    {breakpoint:{width:950,viewsByWidth:3}},
    {breakpoint:{width:1300,viewsByWidth:5}},
]
for (let i = 0; i < responsive.length; i++) {
    if (window.innerWidth>responsive[i].breakpoint.width) {
        viewsByWidth = responsive[i].breakpoint.viewsByWidth;
    }
}

var swiper = new Swiper('.swiper-container', {
    slidesPerView: viewsByWidth,
    spaceBetween: 30,
    
    freeMode: true,
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