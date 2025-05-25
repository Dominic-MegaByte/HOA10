window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.side-nav a');
    
    let current = '';
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (scrollY >= sectionTop - 100) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  });

function changeImage(src, desc) {
    document.getElementById('main-img').src = src;
    document.getElementById('main-img-desc').textContent = desc;
}

function toggleCard(element, image) {
    if (element.classList.contains('active')) {
        element.classList.remove('active');
        element.innerHTML = element.dataset.name;
    } else {
        element.dataset.name = element.innerHTML;
        element.classList.add('active');
        element.innerHTML = `<img src="${image}" alt="">`;
        element.querySelector('img').style.display = 'block';
    }
}



