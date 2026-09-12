// 現在見ているところを、左のメニューに小さく表示します。
const pageLoadItems = document.querySelectorAll('.masthead, .sidebar, main > section, main > footer, .bottom-line');
pageLoadItems.forEach((item, index) => {
  item.classList.add('page-load-item');
  item.style.setProperty('--load-delay', `${index * 120}ms`);
});
requestAnimationFrame(() => document.body.classList.add('page-loaded'));

const navigationLinks = [...document.querySelectorAll('.site-nav a')];
const watchedSections = ['top', 'diary', 'now', 'works', 'links']
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
