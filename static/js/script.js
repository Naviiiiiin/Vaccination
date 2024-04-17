// Navigation Menu
const navLinks = document.getElementById("navLinks");

function showMenu() {
    navLinks.style.right = "0";
}

function hideMenu() {
    navLinks.style.right = "-200px";
}

// Carousel (jQuery)
$(document).ready(function() {
    $(".owl-carousel").owlCarousel({
        loop: true,
        margin: 10,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 3,
                nav: false,
                loop: false
            }
        }
    });
});

// Accordion
document.querySelectorAll('.accordian').forEach(accordian => {
    accordian.addEventListener('click', () => {
        const icon = accordian.querySelector('.icon');
        const answer = accordian.querySelector('.answer');
        
        if (icon.classList.contains('active')) {
            icon.classList.remove('active');
            answer.style.maxHeight = null;
        } else {
            icon.classList.add('active');
            answer.style.maxHeight = answer.scrollHeight + 'px';
        }
    });
});

// Counter Animation
function startCountUpAnimation() {
    const counters = document.querySelectorAll('.count-up');
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText.split('+')[0];
            const speed = 500;
            const inc = target / speed;
            
            if (count < target) {
                counter.innerText = Math.ceil(count + inc) + '+';
                setTimeout(updateCount, 5);
            } else {
                counter.innerText = target + '+';
            }
        };
        updateCount();
    });
}

window.addEventListener('scroll', () => {
    const vaccinationStatsSection = document.getElementById('vaccination-stats');
    if (isInViewport(vaccinationStatsSection)) {
        startCountUpAnimation();
        window.removeEventListener('scroll', startCountUpAnimation);
    }
});
