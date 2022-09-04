const scroll1 = document.getElementById("scroll1")
const scroll2 = document.getElementById("scroll2")
const ContainerBurger = document.getElementById("container_burger");
const Burger = document.getElementById("burger");
const RightAside = document.getElementById("right_aside");
const ProfileData = document.getElementById("profile_data");
const GenreContainer = document.getElementById("genre_container");
const FavoriteContainer = document.getElementById("favorite_container");
const LoginContainer = document.getElementById("login_container");
const RightAsideContainer = document.getElementById("right_aside_container");
const ContentSite = document.getElementById("content")

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

window.onload = function () {
    const AddFavorite = document.getElementsByClassName("add_favorite");
    for (let el of AddFavorite) {
        el.onclick = function () {

            let slug = el.dataset.slug
            el.style.display = "none"
            fetch('api/addfavorite/' + slug + '/', {
                method: "PUT",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },

            });

        }
    }
}


ContainerBurger.onclick = function click() {
    if (RightAside.style.width === "350px") {
        // LeftMenuContainer.style.width = null;
        RightAside.style.width = "75px";
        RightAsideContainer.style.display = "none"
        // ProfileData.style.display = "none"
        // GenreContainer.style.display = "none"
        // FavoriteContainer.style.display = "none"
        // LoginContainer.style.display = "none"
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
        RightAsideContainer.style.display = "flex"
        // ProfileData.style.display = "flex"
        // GenreContainer.style.display = "block"
        // FavoriteContainer.style.display = "block"
        // LoginContainer.style.display = "block"
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


function activescroll(event, scroll) {
    let lastX = event.pageX

    function scrollactive(x) {
        if (x < lastX) {
            scroll.scrollBy({
                top: 0,
                left: (lastX - x) / 8,
                behavior: 'auto'
            });
        } else {
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

    document.onmouseup = function () {
        document.removeEventListener('mousemove', onMouseMove);
        document.onmouseup = null;
    };
    document.addEventListener('mousemove', onMouseMove);
    scroll.ondragstart = function () {
        return false;
    };
    scroll.onselectstart = function () {
        return false;
    };
}


if (scroll1) {
    
    scroll1.onmousedown = function (event) {
        activescroll(event, scroll1)
    };


    scroll2.onmousedown = function (event) {
        activescroll(event, scroll2)
    };
}


window.addEventListener("load", function () {
    let scroll = localStorage.getItem("lastScroll");
    if (!scroll) return false;
    if (window.location.href === localStorage.getItem("lastURL")) {
        ContentSite.scrollBy({
            top: scroll,
            left: 0,
            behavior: 'auto'
        });
        localStorage.removeItem("lastScroll")
        localStorage.removeItem("lastURL")
    }
});


function checkscroll() {
    let scrollTop = ContentSite.scrollTop;
    console.log(scrollTop);
    localStorage.setItem("lastScroll", scrollTop);
    localStorage.setItem("lastURL", window.location.href);
}


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