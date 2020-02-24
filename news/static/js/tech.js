import '../css/tech.css'

const mixmag = document.querySelector(".mixmag");
const factmag = document.querySelector(".factmag");
const menu = document.querySelector(".menu");
const navMobile = document.querySelector(".nav-mobile");
const body = document.querySelector("body");
const magazines = document.querySelectorAll(".magazine");

let activeMag;

async function getData(magazine){
    const response = await fetch(`${document.URL.slice(0,-5)}${magazine}/tech/`);
    const dados = await response.json();

    return dados;
}

function activateMobileUI() {
    magazines.forEach(magazine => {
        if (!magazine.classList.contains(activeMag)) {
            magazine.classList.add("nada") 
        } else {
            magazine.classList.remove("nada");
        }
    });
    menu.style.display = 'block';
}

function landscapeUI() {
    magazines.forEach(magazine => {
        if (magazine.classList.contains('nada')) {
            magazine.classList.remove('nada');
        }
        menu.style.display = 'none'
    });
}


if (localStorage.getItem('activeMag') == 'factmag' || localStorage.getItem('activeMag') == 'mixmag') {
    activeMag = localStorage.getItem('activeMag');
} else {
    activeMag = 'factmag';
}


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

function populateMixMag(data) {
    let arrayTags = JSON.parse(data.tags);
    let tags;
    if (arrayTags.length >= 4) {
        tags = arrayTags.slice(0, 3).toString();
    } else {
        tags = arrayTags.toString();
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

getData("mixmag").then(data => {
    console.log(data, JSON.parse(data[4].tags), typeof JSON.parse(data[4].tags));
    data.forEach(dados => {
        console.log(dados.tags, typeof dados.tags)
        populateMixMag(dados);
    });
}).catch(err => console.log(err))

getData("factmag").then(data => {
    data.forEach(dados => populateFactMag(dados));
}).catch(err => console.log(err))

let res = window.matchMedia("(max-width: 560px)")

window.addEventListener("resize", () => {
    if (res.matches) {
        activateMobileUI();
    } else {
        landscapeUI();
    }
});

if (res.matches) {
    activateMobileUI();
}

navMobile.addEventListener("click", e => {
    if (e.target.title){
    activeMag = e.target.title;
    localStorage.setItem("activeMag", e.target.title);
    activateMobileUI();
    }
});

menu.addEventListener("click", e => {
    e.stopPropagation();
    if(navMobile.classList.contains('nada')) {
        navMobile.classList.remove('nada')
    } else {
        navMobile.classList.add('nada');
    }
});

body.addEventListener("click", e => {
    e.stopPropagation();
    if(!navMobile.classList.contains('nada')) {
        navMobile.classList.add('nada');
    }
});