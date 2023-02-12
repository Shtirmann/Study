const blinds = document.querySelector('.blinds');
const imgs = blinds.querySelectorAll('.blinds__img');
const blindsWidth = blinds.clientWidth;
const amount = 12;
const distance = 10;
const width = (blindsWidth - (amount - 1) * distance) / amount;
let number = 0;

for (let i = 0; i < amount; i++) {
    const span = document.createElement('span');
    const x = i * (width + distance);

    span.style.position = 'absolute';
    span.style.width = width + 'px';
    span.style.left = x + 'px';
    span.style.backgroundSize = blindsWidth + 'px auto';
    span.style.backgroundPosition = -x + 'px 50%';

    blinds.appendChild(span);
}

const spans = blinds.querySelectorAll('span');
animateBlinds();

function animateBlinds() {
    imgs[number].classList.add('blinds__img_active');
    const src = imgs[number].src;

    for (let i = 0; i < amount; i++) {
        spans[i].style.backgroundImage = 'url(' + src + ')';
        const max = 100 - random(0, 40);

        animate(
            1000,
            s => spans[i].style.height = s * max + '%',
            s => s,
            () => animate(
                1000,
                s => spans[i].style.height = max - s * max + '%',
                s => s,
                () => {
                    if (i === amount - 1) {
                        imgs[number].classList.remove('blinds__img_active');
                        number = number === imgs.length - 1 ? 0 : number + 1;
                        animateBlinds();
                    }
                }
            )
        )
    }
}

function random(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}


function animate(
    duration, draw, timing = stateTime => stateTime,
    complete = () => { }
) {
    const startTime = performance.now();

    const f = currentTime => {
        let stateTime = (currentTime - startTime) / duration;
        stateTime = stateTime > 1 ? 1 : stateTime;

        const stateAnimation = timing(stateTime);
        draw(stateAnimation);

        if (stateTime < 1) {
            requestAnimationFrame(f);
        }

        else {
            complete();
        }

    };

    requestAnimationFrame(f);
}