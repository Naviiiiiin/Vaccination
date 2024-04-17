var navLinks = document.getElementById("navLinks");

function showMenu(){
            navLinks.style.right = "0";
        }

        function hideMenu(){
            navLinks.style.right = "-200px"
        }

$(document).ready(function(){
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

const accordians = document.querySelectorAll('.accordian');

accordians.forEach(accordian => {
  const icon = accordian.querySelector('.icon');
  const answer = accordian.querySelector('.answer');

  accordian.addEventListener('click', () => {
    if(icon.classList.contains('active')){
      icon.classList.remove('active');
      answer.style.maxHeight = null;
    }
    else{
      icon.classList.add('active');
      answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  })
})
const isInViewport = (element) => {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
};

// Function to start count-up animation when element is in viewport
const startCountUpAnimation = () => {
  const counters = document.querySelectorAll('.count-up');

  counters.forEach(counter => {
    const updateCount = () => {
      const target = +counter.getAttribute('data-target');
      const count = +counter.innerText.split('+')[0];

      const speed = 500; // Change speed as needed (lower value = slower)

      const inc = target / speed;

      if (count < target) {
        counter.innerText = Math.ceil(count + inc) + '+';
        setTimeout(updateCount, 5); // Increase timeout value for slower animation
      } else {
        counter.innerText = target + '+';
      }
    };

    updateCount();
  });
};

// Add event listener to scroll event
window.addEventListener('scroll', () => {
  const vaccinationStatsSection = document.getElementById('vaccination-stats');
  if (isInViewport(vaccinationStatsSection)) {
    // Start count-up animation if section is in viewport
    startCountUpAnimation();
    // Remove event listener after animation has started
    window.removeEventListener('scroll', startCountUpAnimation);
  }
});