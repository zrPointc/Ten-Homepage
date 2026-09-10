// 現在見ているところを、左のメニューに小さく表示します。
const navigationLinks = [...document.querySelectorAll('.site-nav a')];
const watchedSections = ['top', 'diary', 'works', 'memo', 'links']
  .map((id) => document.getElementById(id));
let scheduled = false;
function updateNavigation() {
  scheduled = false;
  let current = 'top';
  for (const section of watchedSections.slice(1)) {
    if (section.getBoundingClientRect().top <= window.innerHeight * 0.45) current = section.id;
  }
  if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 10) current = 'links';
  for (const link of navigationLinks) {
    const active = link.getAttribute('href') === '#' + current;
    link.classList.toggle('active', active);
    if (active) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}
window.addEventListener('scroll', () => {
  if (!scheduled) { scheduled = true; window.requestAnimationFrame(updateNavigation); }
}, { passive: true });
window.addEventListener('resize', updateNavigation);
updateNavigation();
