const navToggle = document.querySelector('.nav-toggle')
const nav = document.querySelector('.nav')

navToggle.addEventListener('click',() => {
    nav.classList.toggle('nav-visible')
})


const navLink = document.querySelectorAll('.nav__link')

const linkAction = () => {
    const navMenu = document.querySelector('.nav')
    navMenu.classList.remove('nav-visible') 
}
navLink.forEach(n => n.addEventListener('click', linkAction))


//portfolio
const portfolioItem = document.querySelectorAll('.portfolio__item')
const portfolioProject = document.querySelectorAll('.portfolio__project')

portfolioItem.forEach( (item) => {
    item.addEventListener('click', () => {
       portfolioItem.forEach( (itemlist) =>{
            itemlist.classList.remove('active')
       })
       item.classList.add('active')
       const dataFilter = item.getAttribute('data-filter')
       portfolioProject.forEach( ( portfoliopro ) =>{
           portfoliopro.classList.add('hide')
           if(portfoliopro.getAttribute('data-item') == dataFilter || dataFilter=='all'){
            portfoliopro.classList.remove('hide')
           }
       } )
    })
})

//Scroll Header

function scrollHeader(){
    const header = document.getElementById('header')
    if(this.scrollY >= 80) header.classList.add('scroll-header'); else header.classList.remove('scroll-header') 
}
window.addEventListener('scroll',scrollHeader)

function scrollUp(){
    const scrollUp = document.getElementById('scroll-up');
    if(this.scrollY >= 560) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll')
}

window.addEventListener('scroll',scrollUp)


// //Dark Theme

// const themeButton = document.getElementById('theme-button');

// const darkTheme = 'dark-theme'
// const iconTheme = 'bx-toggle-right'


// const selectedTheme = localStorage.getItem('selected-theme')
// const selectedIcon = localStorage.getItem('selected-icon')

// const getCuttentTheme = () => document.body.classList.contains(darkTheme) ? 'dark':'light'
// const getCuttentIcon = () => themeButton.classList.contains(icontheme) ? 'bx-toggle-left':'bx-toggle-right'

// if(selectedTheme){
//     document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
//     themeButton.classList[selectedIcon === 'bx-toggle-left' ? 'add' : 'remove'](iconTheme)
// }
// themeButton.addEventListener('click', () => {
//     console.log('whaaaaaaaaaat')
//     document.body.classList.toggle(darkTheme)
//     themeButton.classList.toggle(iconTheme)
//     localStorage.setItem('selected-icon', getCuttentIcon())
//     localStorage.setItem('selected-theme', getCuttentTheme())
// })

/*=============== DARK LIGHT THEME ===============*/
const themeButton = document.getElementById('theme-button')
const darkTheme = 'dark-theme'
const iconTheme = 'bx-toggle-right'

// Previously selected topic (if user selected)
const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')

// We obtain the current theme that the interface has by validating the dark-theme class
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx-toggle-left' : 'bx-toggle-right'

// We validate if the user previously chose a topic
if (selectedTheme) {
  // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
  document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
  themeButton.classList[selectedIcon === 'bx-toggle-left' ? 'add' : 'remove'](iconTheme)
}

// Activate / deactivate the theme manually with the button
themeButton.addEventListener('click', () => {
    // Add or remove the dark / icon theme
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)
    // We save the theme and the current icon that the user chose
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})