//now start drag & drop system
const dropArea = document.querySelectorAll('.imgo');
let file;
button = document.querySelectorAll('.browse');
inputFile = document.querySelectorAll('.file');

const dragText = document.querySelectorAll('.contant');

dropArea.forEach((value,index)=>{
    button[index].onclick = ()=>{
        inputFile[index].click();
    }
    inputFile[index].addEventListener('change',function(){
        file = this.files[0];
        showFile(index);
    });
    
    dropArea[index].addEventListener('dragover',(event)=>{
        dropArea[index].classList.add('act');
        event.preventDefault();
    });
    
    dropArea[index].addEventListener('dragleave',(event)=>{
        dropArea[index].classList.remove('act');
        event.preventDefault();
    });
    
    dropArea[index].addEventListener('drop',(event)=>{
        event.preventDefault();
        file = event.dataTransfer.files[0];
        showFile(index);
    });
})

function showFile(index){

    let fileType = file.type;
    let url = URL.createObjectURL(file);
    let validExtensions = ["image/jpeg","image/jfif","image/png","image/jpg"];

    if (validExtensions.includes(fileType)) {

        let imgTag = `<img class="imgo1 active" src="${url}" alt="">`;
        dragText[index].innerHTML = imgTag;
        dropArea[index].classList.add('act');
        let images = document.querySelectorAll('.imgo1');
        
        images[index].addEventListener('click',()=>{   
            document.getElementById('main').src = images[index].src;
        });

        images[index].addEventListener('dblclick',()=>{   
            inputFile[index].click();
            
            inputFile[index].addEventListener('change',function(){
                file = this.files[0];
                showFile(index);
            });
        });
        
        images[index].addEventListener('mouseover',()=>{   
            document.getElementById('main').src = images[index].src;
        });

    } else {

        alert('This is not a Image..\n Select a proper Image for upload...');
        dropArea.classList.remove('act');

    }
}
