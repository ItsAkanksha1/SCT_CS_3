# Advanced Password Checker - Streamlit Web App

import streamlit as st
import string
import math
import requests
import re
import time
import json
from difflib import SequenceMatcher
from collections import deque

# ---- Configurations ----
PASSWORD_HISTORY_LIMIT = 10
COMMON_PASSWORDS = set([
    "123456", "password", "123456789", "12345678", "12345",
    "111111", "1234567", "sunshine", "qwerty", "iloveyou"
])
HIBP_API = "https://api.pwnedpasswords.com/range/"

# ---- Session state to store password history ----
if 'password_history' not in st.session_state:
    st.session_state.password_history = deque(maxlen=PASSWORD_HISTORY_LIMIT)

# ---- Helper Functions ----
def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in string.punctuation for c in password): charset += len(string.punctuation)
    if charset == 0: return 0
    return round(len(password) * math.log2(charset), 2)

def is_blacklisted(password):
    return password.lower() in COMMON_PASSWORDS

def check_keyboard_pattern(password):
    patterns = ["qwerty", "asdfgh", "zxcvbn", "123456"]
    return any(pat in password.lower() for pat in patterns)

def check_breach(password):
    sha1pwd = password.encode('utf-8')
    sha1pwd = sha1pwd.hex()
    prefix = sha1pwd[:5].upper()
    try:
        res = requests.get(HIBP_API + prefix)
        if res.status_code != 200:
            return False
        hashes = res.text.splitlines()
        for line in hashes:
            if sha1pwd[5:].upper() in line:
                return True
    except:
        pass
    return False

def suggest_improvements(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters.")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include numbers.")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Include special characters.")
    if is_blacklisted(password):
        suggestions.append("Avoid common passwords.")
    if check_keyboard_pattern(password):
        suggestions.append("Avoid keyboard patterns.")
    return suggestions

def get_strength_score(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if not is_blacklisted(password): score += 1
    if not check_keyboard_pattern(password): score += 1
    entropy = calculate_entropy(password)
    if entropy > 50: score += 1
    return score

def get_strength_label(score):
    if score <= 2: return "Very Weak", "red"
    elif score <= 4: return "Weak", "orange"
    elif score <= 6: return "Strong", "blue"
    else: return "Very Strong", "green"

# ---- Web UI ----
st.set_page_config(page_title="Advanced Password Checker", layout="centered")
st.title("🔐 Advanced Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    st.session_state.password_history.append(password)
    score = get_strength_score(password)
    strength, color = get_strength_label(score)
    entropy = calculate_entropy(password)

    st.markdown(f"**Strength**: :{color}[{strength}] ({score}/8)")
    st.progress(score / 8)

    st.markdown(f"**Entropy**: {entropy} bits")

    if is_blacklisted(password):
        st.warning("This password is commonly used and easily guessable.")

    if check_keyboard_pattern(password):
        st.warning("Avoid common keyboard patterns.")

    if check_breach(password):
        st.error("⚠️ This password has appeared in a data breach!")

    suggestions = suggest_improvements(password)
    if suggestions:
        st.markdown("### Suggestions to improve:")
        for s in suggestions:
            st.markdown(f"- {s}")

    if len(st.session_state.password_history) > 1:
        last_pwd = st.session_state.password_history[-2]
        sim_ratio = SequenceMatcher(None, last_pwd, password).ratio()
        if sim_ratio > 0.8:
            st.warning("Your new password is very similar to the previous one.")

    # Localization (example placeholder only)
    lang = st.selectbox("Language", ["English", "Hindi", "Spanish"], index=0)
    st.markdown(f"_Localization selected: {lang}_")
