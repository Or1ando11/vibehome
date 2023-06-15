let showMore = true;
    
function toggleAdditionalOptions() {
  const additionalOptions = document.querySelectorAll('.additional-options');
  additionalOptions.forEach(option => option.classList.toggle('hidden'));

  const showMoreButton = document.querySelector('.show-more-button');
  showMore = !showMore;
  if (showMore) {
    showMoreButton.textContent = 'WIĘCEJ OPCJI';
  } else {
    showMoreButton.textContent = 'MNIEJ OPCJI';
  }
}