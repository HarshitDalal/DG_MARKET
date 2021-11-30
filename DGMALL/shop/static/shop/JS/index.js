const manu = document.querySelector('.manu-icon');
const close1 = document.querySelector('.close-icon');
manu.addEventListener('click',()=>{
  document.querySelector('.nav').classList.add('manu-active');
  manu.classList.add('close');
  close1.classList.add('on');
});

close1.addEventListener('click',()=>{
  document.querySelector('.nav').classList.remove('manu-active');
  manu.classList.remove('close');
  close1.classList.remove('on');
});