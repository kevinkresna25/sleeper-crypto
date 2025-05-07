document.addEventListener('DOMContentLoaded', () => {
    const algSelect = document.getElementById('algorithm');
    const keyGroup  = document.getElementById('key-group');
    const keyLabel  = document.getElementById('key-label');
    const keyInput  = document.getElementById('key');
    const output    = document.getElementById('output-text');
    const btn       = document.getElementById('process-btn');
  
    function updateKeyField() {
      const alg = algSelect.value;
      if (alg === 'caesar') {
        keyLabel.textContent = 'Shift (angka)';
        keyInput.type       = 'number';
        keyInput.placeholder= 'Masukkan jumlah pergeseran...';
        keyGroup.style.display = 'block';
      } else if (['rc4','aes','des'].includes(alg)) {
        keyLabel.textContent = 'Kunci';
        keyInput.type       = 'text';
        keyInput.placeholder= 'Masukkan kunci...';
        keyGroup.style.display = 'block';
      } else {
        keyGroup.style.display = 'none';
      }
    }
  
    algSelect.addEventListener('change', updateKeyField);
    updateKeyField();
  
    btn.addEventListener('click', async () => {
      const payload = {
        text:      document.getElementById('input-text').value,
        algorithm: algSelect.value,
        mode:      document.getElementById('mode').value,
        key:       keyInput.value
      };
      try {
        const resp = await fetch('/api/process', {
          method: 'POST',
          headers: {'Content-Type':'application/json'},
          body: JSON.stringify(payload)
        });
        const data = await resp.json();
  
        if (data.error) {
          output.value = 'Error: ' + data.error;
          output.classList.add('is-invalid');
        } else {
          output.value = data.result;
          output.classList.remove('is-invalid');
        }
      } catch (e) {
        output.value = 'Error: ' + e.message;
        output.classList.add('is-invalid');
      }
    });
  });
  