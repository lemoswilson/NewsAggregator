import '../css/styles.css';

const residentAdvisor = document.querySelector(".resident-advisor");
const mixmag = document.querySelector(".mixmag");
const factmag = document.querySelector(".factmag");
const pitchfork = document.querySelector(".pitchfork");

async function getData(magazine){
    const response = await fetch(`${document.URL}${magazine}/news`);
    const dados = await response.json();

    return dados;
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
        tags = arrayTags.slice(0, 2).toString()
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
    console.log(data[1].date, data[1].headline)
    data.forEach(dados => populateMixMag(dados));
}).catch(err => console.log(err))

getData("pitchfork").then(data => {
    data.forEach(dados => populatePitchfork(dados));
}).catch(err => console.log(err))