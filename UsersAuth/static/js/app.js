console.log('hello you')

const body = document.querySelector('.body')
let lastScroll = 0

window.addEventListener('scroll', () =>{
    const currentScroll = window.pageYOffset

    if ( currentScroll <= 0) {
        body.classList.remove("scroll-up")
    }

    if (currentScroll > lastScroll && !body.classList.contains("scroll-down")) {
        body.classList.remove("scroll-up")
        body.classList.add("scroll-down")
    } 

    lastScroll = currentScroll
})