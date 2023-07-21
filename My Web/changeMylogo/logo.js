var myImage = document.getElementById("logo");

function changeImage(){
    var image = document.getElementsByName("choice");
    var val= "";
    // console.log(image[3].value);
    for (var i = 0, length = image.length; i < length; i++) {
        if (image[i].checked) {
            val = image[i].value; 
            break;
        }
    }
    if (val == "Apple"){
        myImage.src = "apple.png";
    } 
    else if (val == "Google"){
        myImage.src = "google.png";
    }
    else if (val == "Twitter"){
        myImage.src = "twitter.png";
    }
    else if (val == "Jiangshan"){
        myImage.src = "Studio-Project.png";
    }

}
