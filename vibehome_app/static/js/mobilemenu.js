const button = document.querySelector('.mobile-menu-button');
const menuContainer = document.querySelector('.mobile-menu-container');
const menu = document.querySelector('.mobile-menu');

let isMenuOpen = false; // Dodatkowa zmienna, która będzie śledzić stan menu

function toggleMenuVisibility() {
  if (window.innerWidth >= 768) {
    menu.classList.add('hidden');
    isMenuOpen = false; // Ustawienie stanu menu na zamknięte
  } else {
    if (isMenuOpen) {
      menu.classList.remove('hidden');
    } else {
      menu.classList.add('hidden');
    }
  }
}

button.addEventListener('click', () => {
  menu.classList.toggle('hidden');
  isMenuOpen = !isMenuOpen; // Odwrócenie stanu menu po kliknięciu
});

window.addEventListener('resize', toggleMenuVisibility);


window.addEventListener('load', () => {
  toggleMenuVisibility(); // Wywołanie funkcji toggleMenuVisibility() po załadowaniu strony

  if (window.innerWidth < 768) {
    menuContainer.classList.add('hidden');
  } else {
    menuContainer.classList.remove('hidden');
  }
});
