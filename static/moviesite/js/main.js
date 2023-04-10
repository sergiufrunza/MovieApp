const scroll1 = document.getElementById("scroll1")
const scroll2 = document.getElementById("scroll2")
const ContainerBurger = document.getElementById("container_burger");
const Burger = document.getElementById("burger");
const RightAside = document.getElementById("right_aside");
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


function AddFavorite(el){
    let slug = el.dataset.slug
    el.style.display = "none"
    fetch('/api/favorite/' + slug + '/', {
        method: "PUT",
        headers: {
            'X-CSRFToken': getCookie("csrftoken")
        },

    });
}

async function DeleteFavorite(el){
    let slug = el.dataset.slug
   await fetch('/api/favorite/' + slug + '/', {
                method: "DELETE",
                        headers: {
            'X-CSRFToken': getCookie("csrftoken")
        },
            });
    el.style.display = "none"
    let scrollTop = ContentSite.scrollTop;
    localStorage.setItem("lastScroll", scrollTop);
    localStorage.setItem("lastURL", window.location.href);
    document.location.reload()
}



function Checkinputtype(el) {
    elparent = el.parentNode.querySelector("#password")
    if (elparent.type === "password") {
        el.style.color = "var(--accent)"
        elparent.type = "text"
    } else {
        el.style.color = "var(--secondary-color)"
        elparent.type = "password"
    }
}


ContainerBurger.onclick = function click() {
    if (RightAside.style.width === "350px") {
        RightAside.style.width = "75px";
        RightAsideContainer.style.display = "none"
        Burger.classList.toggle("burger");
        Burger.classList.toggle("burger_active");
    } else {
        RightAside.style.width = "350px";
        RightAsideContainer.style.display = "flex"
        Burger.classList.toggle("burger_active");
        Burger.classList.toggle("burger");
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
    localStorage.setItem("lastScroll", scrollTop);
    localStorage.setItem("lastURL", window.location.href);
}
