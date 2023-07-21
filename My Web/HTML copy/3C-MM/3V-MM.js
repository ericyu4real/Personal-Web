const imageInput=document.querySelector("#imageInput");
let uploadImage="";

function uppy() {
    const reader = new FileReader();
    reader.addEventListener("load", ()=>{
        uploadImage=reader.result;
        document.querySelector("#displayImage").style.backgroundImage = `url(${uploadImage})`;
    });
    reader.readAsDataURL(this.files[0]);
}
imageInput.addEventListener("change", uppy);