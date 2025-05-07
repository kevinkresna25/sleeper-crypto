(function() {
    const starfield = document.getElementById('starfield');
    if (!starfield) return;
    for (let i = 0; i < 200; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      star.style.top  = `${Math.random() * 100}%`;
      star.style.left = `${Math.random() * 100}%`;
      starfield.appendChild(star);
    }
  })();
  
  (function() {
    let lastTime = 0;
    document.addEventListener('mousemove', e => {
      const now = Date.now();
      if (now - lastTime < 30) return;
      lastTime = now;
  
      const p = document.createElement('div');
      p.className = 'cursor-particle';
      p.style.left = `${e.clientX}px`;
      p.style.top  = `${e.clientY}px`;
      document.body.appendChild(p);
  
      p.addEventListener('animationend', () => p.remove());
    });
  })();
