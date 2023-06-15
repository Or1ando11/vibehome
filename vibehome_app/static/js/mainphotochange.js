var photos = document.getElementsByClassName('photo');
var index = 0;

setInterval(function() {
    photos[index].classList.remove('active');
    index = (index + 1) % photos.length;
    photos[index].classList.add('active');
}, 5000);