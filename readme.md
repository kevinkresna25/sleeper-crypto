# SleeperCrypto

> A modern, dark-themed Flask web app for encrypting and decrypting text  
> using Caesar Cipher, RC4, AES (CBC) and DES (CBC)

---

## 🎯 Features

- **Caesar Cipher** (shift-based)
- **RC4** stream cipher
- **AES-128 CBC** (key derived via MD5)
- **DES CBC** (key derived via MD5)

---

## 📂 Project Structure

```

sleeper-crypto/
├── app/
│   ├── __init__.py             # Flask application factory
│   ├── routes.py               # HTTP routes and API endpoints
│   ├── crypto.py               # Encryption/decryption logic
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Custom styles
│   │   ├── js/
│   │   │   ├── main.js         # UI logic & fetch calls
│   │   │   └── animations.js   # Starfield & cursor particles
│   │   └── images/
│   │       ├── logo-dark.png
│   │       └── logo-white.png
│   └── templates/
│       └── index.html          # Main HTML template
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Docker Compose orchestration
├── start.sh                    # Convenience script to build & run
├── requirements.txt            # Python dependencies
└── LICENSE

```

---

## 🛠️ Prerequisites

- **Docker** v20+  
- **Docker Compose** v1.29+  

---

## 🚀 Quick Start

1. **Clone repository**

   ```bash
   git clone https://github.com/username/sleeper-crypto.git
   cd sleeper-crypto
   ```

2. **Run with Docker**

   ```bash
   ./start.sh
   ```

   > This script will stop any running containers, prune old images,
   > then rebuild & start the app in detached mode.

---

## 💻 Local Development

1. Buat dan aktifkan virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan Flask

   ```bash
   cd app
   export FLASK_APP=app
   flask run --host=0.0.0.0 --port=5000
   ```

---

## ⚙️ Configuration & Customization

* **Static assets**: `app/static/css`, `app/static/js`, `app/static/images`
* **Templates**: `app/templates/index.html` (Jinja2)
* **Algorithms**: `app/crypto.py`

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ❤️ Acknowledgments

* [Flask](https://flask.palletsprojects.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Chepy](https://pypi.org/project/chepy/) for cryptographic building blocks
