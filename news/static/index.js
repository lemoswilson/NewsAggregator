// import '../css/styles.css';

const residentAdvisor = document.querySelector(".resident-advisor");
const mixmag = document.querySelector(".mixmag");
const factmag = document.querySelector(".factmag");
const pitchfork = document.querySelector(".pitchfork");
const menu = document.querySelector(".menu");
const navMobile = document.querySelector(".nav-mobile");
const body = document.querySelector("body");
let magazines = document.querySelectorAll(".magazine");

let activeMag;


async function getData(magazine){
    const response = await fetch(`${document.URL}${magazine}/news`);
    const dados = await response.json();

    return dados;
}

function activateMobileUI() {
    magazines.forEach(magazine => {
        if (!magazine.classList.contains(activeMag)) {
            magazine.classList.add("nada");
        } else {
            magazine.classList.remove("nada");
        }
});
    menu.style.display = 'block';
}

function landscapeUI() {
    magazines.forEach(magazine => {
        if(magazine.classList.contains('nada')) {
            magazine.classList.remove('nada');
        }
        menu.style.display = 'none'; 
    });
}


if (!localStorage.getItem('activeMag')) {
    activeMag = 'factmag';
} else {
    activeMag = localStorage.getItem('activeMag');
}

// JSON.parse(dados[3].tags).forEach(data => console.log(data));

function populateFactMag(data) {
    let innerT = `<li class="news">
                            <article>
                                <div class="headline">
                                    <h2><a href="${data.link}">${data.headline}</a></h2>
                                </div>
                                <div class="description">
                                    <p><a href="${data.link}">${data.description}</a></p>
                                </div>
                                <div class="meta">
                                    <ul>
                                        <li class="date"><time datetime="${data.date}">${data.date.split("T")[0]}</time></li>
                                        <li>|</li>
                                        <li class="tags">${JSON.parse(data.tags).toString()}</li>
                                    </ul>
                                </div>
                            </article>
                            </li>
`;
    factmag.querySelector(".news-list").innerHTML += innerT;
}

function populateResidentAdvisor(data) {
    let innerT = `<li class="news">
    <article>
        <div class="headline">
            <h2><a href="${data.link}">${data.headline}</a></h2>
        </div>
        <div class="description">
            <p><a href="${data.link}">${data.description}</a></p>
        </div>
        <div class="meta">
            <ul>
                <li class="date"><time datetime="${data.date}">${data.date.split("T")[0]}</time></li>
                <li>|</li>
                <li class="tags">${data.tags}</li>
            </ul>
        </div>
    </article>
    </li>
`;
residentAdvisor.querySelector(".news-list").innerHTML += innerT;
}

function populateMixMag(data) {
    let arrayTags = JSON.parse(data.tags)
    let tags;
    if (arrayTags.length >= 4) {
        tags = arrayTags.slice(0, 3).toString()
    } else {
        tags = arrayTags.toString()
    }
    let innerT = `<li class="news">
                            <article>
                                <div class="headline">
                                    <h2><a href="${data.link}">${data.headline}</a></h2>
                                </div>
                                <div class="description">
                                    <p><a href="${data.link}">${data.description}</a></p>
                                </div>
                                <div class="meta">
                                    <ul>
                                        <li class="date"><time datetime="${data.date}">${data.date.split("T")[0]}</time></li>
                                        <li>|</li>
                                        <li class="tags">${tags}</li>
                                    </ul>
                                </div>
                            </article>
                            </li>
`;
    mixmag.querySelector(".news-list").innerHTML += innerT;
}

function populatePitchfork(data) {
    let innerT = `<li class="news">
                            <article>
                                <div class="headline">
                                    <h2><a href="${data.link}">${data.headline}</a></h2>
                                </div>
                                <div class="description">
                                    <p><a href="${data.link}">${data.description}</a></p>
                                </div>
                                <div class="meta">
                                    <ul>
                                        <li class="date"><time datetime="${data.date}">${data.date.split("T")[0]}</time></li>
                                        <li>|</li>
                                        <li class="tags">${JSON.parse(data.tags).toString()}</li>
                                    </ul>
                                </div>
                            </article>
                            </li>
`;
    pitchfork.querySelector(".news-list").innerHTML += innerT;
}

getData("factmag").then(data => {
    data.forEach(dados => populateFactMag(dados));
}).catch(err => console.log(err))

getData("residentadvisor").then(data => {
    data.forEach(dados => populateResidentAdvisor(dados));
}).catch(err => console.log(err))

getData("mixmag").then(data => {
    data.forEach(dados => populateMixMag(dados));
}).catch(err => console.log(err))

getData("pitchfork").then(data => {
    data.forEach(dados => populatePitchfork(dados));
}).catch(err => console.log(err))

let res = window.matchMedia("(max-width: 560px)")

window.addEventListener("resize", () => {
    console.log("being resized");
    if (res.matches) {
        activateMobileUI();
    } else {
        landscapeUI();
    }     
});

// if (window.innerHeight > window.innerWidth) {
//     activateMobileUI();
// }

if (res.matches) {
    activateMobileUI();
}

menu.addEventListener("click", e => {
    e.stopPropagation();
    if(navMobile.classList.contains('nada')) {
        navMobile.classList.remove('off');
        navMobile.classList.add('animate');
        navMobile.classList.remove('nada');
    } else {
        navMobile.classList.remove('animate')
        navMobile.classList.add('off');
        setTimeout(() => navMobile.classList.add('nada'), 300);
    }
});

body.addEventListener("click", e => {
    e.stopPropagation();
    if(!navMobile.classList.contains('nada')) {
        console.log('pressed');
        navMobile.classList.remove('animate');
        navMobile.classList.add('off');
        setTimeout(() => navMobile.classList.add('nada'), 300);
    }
});

navMobile.addEventListener("click", e => {
    if (e.target.title){
    activeMag = e.target.title;
    localStorage.setItem("activeMag", e.target.title);
    activateMobileUI();
    }
});




    



