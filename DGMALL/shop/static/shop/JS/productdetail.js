var images = document.getElementsByClassName('imgo');
for (let ii = 0; ii < images.length; ii++) {
    images[ii].addEventListener('click',()=>{   
        document.getElementById('main').src = images[ii].src;
    });
    images[ii].addEventListener('mouseover',()=>{   
        document.getElementById('main').src = images[ii].src;
    });
}

const tabHeader = document.getElementsByClassName('tab_header')[0];
const tabIndicator = document.getElementsByClassName('indicator')[0];
const tabBody = document.getElementsByClassName('tabs_body')[0];

let array = tabHeader.getElementsByClassName('a');
for (let i = 0; i < array.length; i++) {
    array[i].addEventListener('click',()=>{
        tabHeader.getElementsByClassName('active1')[0].classList.remove('active1');
        array[i].classList.add('active1');
        tabBody.getElementsByClassName('active2')[0].classList.remove('active2');
        tabBody.getElementsByClassName('tbody')[i].classList.add('active2');
        tabIndicator.style.left = `calc(calc(100% / 3) * ${i})`;
    });   
}

const productReal = document.querySelector('#real');
const productDiscount = document.querySelector('#discount');

if (productDiscount.innerHTML.length > 2) {
    productReal.style.textDecoration = 'line-through';
    productDiscount.setAttribute('style','display:block;');
} else {
    productDiscount.setAttribute('style','display:none;');

}