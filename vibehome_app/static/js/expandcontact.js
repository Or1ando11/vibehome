const mobileFormToggle = document.querySelector('.mobile-form-toggle');
const contactForm = document.querySelector('#contact-form');

mobileFormToggle.addEventListener('click', () => {
  mobileFormToggle.classList.toggle('active');
  contactForm.classList.toggle('hidden');
});