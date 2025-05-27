import streamlit as st

# Наш словарь
dictionary = {
    "book": "kitob",
    "pen": "ruchka",
    "apple": "olma",
    "water": "suv",
    "sun": "quyosh",
}

st.title("📘 Inglizcha → O‘zbekcha Lug‘at")

# Ввод слова пользователем
word = st.text_input("So‘zni kiriting (masalan, 'book'):")

# Поиск перевода
if word:
    translation = dictionary.get(word.lower())  # делаем регистр независимым
    if translation:
        st.success(f"Tarjimasi: **{translation}**")
    else:
        st.error("Kechirasiz, bu so‘z lug‘atda topilmadi.")
