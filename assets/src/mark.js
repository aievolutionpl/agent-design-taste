// The AI Evolution Polska hex mark, injected wherever an element has [data-mark].
// The brand gradient (cyan → iris) is used here and nowhere else.
(() => {
  let n = 0;
  for (const el of document.querySelectorAll('[data-mark]')) {
    const id = `mk${n++}`;
    el.insertAdjacentHTML('afterbegin', `<svg viewBox="0 0 48 48" aria-hidden="true">
      <defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#88E5FC"/><stop offset="1" stop-color="#8776F4"/></linearGradient></defs>
      <path d="M24 3.5 41.8 13.75v20.5L24 44.5 6.2 34.25v-20.5Z" fill="#121323" stroke="url(#${id})" stroke-width="2.6" stroke-linejoin="round"/>
      <text x="24" y="29.5" text-anchor="middle" font-family="Sora" font-weight="700" font-size="15" fill="#F4F7FB" letter-spacing=".5">AI</text>
    </svg>`);
  }
})();
