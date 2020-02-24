import '../css/tech.css'

const mixmag = document.querySelector(".mixmag");
const factmag = document.querySelector(".factmag");


async function getData(magazine){
    const response = await fetch(`${document.URL.slice(0,-5)}${magazine}/tech/`);
    const dados = await response.json();

    return dados;
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