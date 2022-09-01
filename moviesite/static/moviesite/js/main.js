const scroll1 = document.getElementById("scroll1")
const scroll2 = document.getElementById("scroll2")
const ContainerBurger = document.getElementById("container_burger");
const Burger = document.getElementById("burger");
const RightAside = document.getElementById("right_aside");
const ProfileData = document.getElementById("profile_data");
const GenreContainer = document.getElementById("genre_container");




ContainerBurger.onclick = function click() {
        if (RightAside.style.width === "350px") {
            // LeftMenuContainer.style.width = null;
            RightAside.style.width = "75px";
            ProfileData.style.display = "none"
            GenreContainer.style.display = "none"
            // ProfileFoto.style.width = "46px"
            // ProfileFoto.style.height = "46px"
            // ProfileFoto.style.borderColor = "#0339fa"
            // LeftMenu.style.alignItems = "end";
            Burger.classList.toggle("burger");
            Burger.classList.toggle("burger_active");
            // profile.style.display = "none";
            // for ( let i=0; i<navItem.length; i++) {
            //     LeftMenuIt[i].style.justifyContent = "end";
            //     navItem[i].style.display = "none";
            // }
        } else {
            // LeftMenuContainer.style.width = "100%";
            RightAside.style.width = "350px";
            ProfileData.style.display = "flex"
            GenreContainer.style.display = "grid"
            // ProfileFoto.style.width = "75px"
            // ProfileFoto.style.height = "75px"
            // ProfileFoto.style.borderColor = "#4d5665"
            Burger.classList.toggle("burger_active");
            Burger.classList.toggle("burger");
            // setTimeout(delay, 200);
            // for ( let element of LeftMenuIt ) {
            //     element.style.justifyContent = "start";
            // }
        }
    }







function activescroll(event, scroll){
    let lastX =event.pageX
  function scrollactive(x) {
    if (x < lastX){
      scroll.scrollBy({
            top: 0,
            left: (lastX - x) / 8,
            behavior: 'auto'
          });
    }
    else{
      scroll.scrollBy({
            top: 0,
            left: (lastX - x) / 8,
            behavior: 'auto'
          });
    }
  }

  function onMouseMove(event) {
    scrollactive(event.pageX);
  }
    document.onmouseup = function() {
    document.removeEventListener('mousemove', onMouseMove);
    document.onmouseup = null;
  };
    document.addEventListener('mousemove', onMouseMove);
    scroll.ondragstart = function() {
  return false;
};
scroll.onselectstart =  function() {
  return false;
};
}


scroll1.onmousedown = function(event) {
    activescroll(event, scroll1)
    };
scroll2.onmousedown = function(event) {
    activescroll(event, scroll2)
    };


















// const GenreList = document.getElementsByClassName("genre");
// const GenreContainer = document.getElementById("genre_container");
//
// GenreContainer.onclick = function click(){
//   for ( let i=0; i<GenreList.length; i++) {
//     document.getElementById("genre__"+(i+1)).onclick = function click(){
//         const IconSelect = document.getElementById("icon_select_"+(i+1))
//         const IconAdd = document.getElementById("icon_add_"+(i+1))
//
//         if(IconAdd.style.display === "block"){
//             IconAdd.style.display = "none"
//             IconSelect.style.display = "block"
//             this.style.background = "#E52327"
//
//         }
//         else{
//             this.style.background = "#151318"
//             IconAdd.style.display = "block"
//             IconSelect.style.display = "none"
//
//         }
//                 }
//                                         }
//                                     }