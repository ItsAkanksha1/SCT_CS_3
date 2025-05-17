# SCT_CS_3
# 🔐 Password Strength Checker

A smart and interactive web app built with **Streamlit** that evaluates the strength of passwords in real-time. It checks for various password security criteria and provides actionable feedback to users to improve their password quality.

---

## 🚀 Features

- ✅ **Real-time Password Strength Meter** (No need to press Enter)
- 📊 **Entropy Calculation** to estimate how guessable the password is
- 🚫 **Blacklist Check** for common passwords (like `123456`, `password`, etc.)
- 💡 **Password Suggestions** to help improve weak passwords
- 🧠 **Keyboard Pattern Detection** to discourage predictable typing patterns
- 📖 **Password History Check** to avoid reusing old passwords (session-based)
- 🌍 **Localization-ready** (Multilingual support placeholder)
- 🧪 **Live Breach Check** using [HaveIBeenPwned API](https://haveibeenpwned.com/API)


## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/password-strength-checker.git
cd password-strength-checker
````

### 2. Install Dependencies

```bash
pip install streamlit requests zxcvbn
```

### 3. Run the App

```bash
streamlit run password_checker.py
```

The app will automatically open in your default web browser.

---

## 🌐 Deployment

You can easily deploy this on platforms like:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Render](https://render.com/)
* [Heroku](https://www.heroku.com/)
* [Railway](https://railway.app/)

Let me know if you want deployment support!

---

## 🙌 Contributing

Contributions are welcome! If you have ideas for new features or enhancements, feel free to fork this project and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🧠 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [HaveIBeenPwned API](https://haveibeenpwned.com/)
* [zxcvbn - Dropbox Password Strength Estimator](https://github.com/dropbox/zxcvbn)

---

Made with ❤️ by Akanksha
