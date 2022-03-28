let sidebar = document.querySelector(".sidebar")
let hamburger = document.querySelector(".hamburger")
let closebtn = document.querySelector(".close")


hamburger.addEventListener("click",()=>{
    sidebar.style.transform ="translateX(0px)";
    if (sidebar.style.transform ="translateX(0px)") {
        hamburger.style.display ="none"
        closebtn.style.display="block"
    }
})

closebtn.addEventListener("click",()=>{
    sidebar.style.transform="translateX(-768px)";
    if (sidebar.style.transform="translateX(-768px)") {
        hamburger.style.display="block"
        closebtn.style.display="none"
    }
})

