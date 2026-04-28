import streamlit as st
import math

st.set_page_config(page_title="Прогноз рецидива лейомиомы", layout="centered")

st.title("📊 Прогнозирование рецидива лейомиомы")
st.write("Расчет вероятности рецидива на основе логистической модели")

st.markdown("### Введите данные пациентки:")

# --- Ввод данных ---
rody = st.radio("Были роды в анамнезе?", ["Да", "Нет"])
dlit = st.radio("Длительность заболевания более 7 лет?", ["Да", "Нет"])
nzo = st.radio("Нарушение жирового обмена (ИМТ > 25)?", ["Да", "Нет"])
amk = st.radio("Аномальное маточное кровотечение в анамнезе?", ["Да", "Нет"])

vozrast = st.number_input("Возраст пациентки (лет)", min_value=18, max_value=70, value=35)
razmer = st.number_input("Размер наибольшего миоматозного узла (см)", min_value=0.0, max_value=20.0, value=3.0)

# --- Кодирование бинарных переменных ---
X_rody = 1 if rody == "Да" else 0
X_dlit = 1 if dlit == "Да" else 0
X_nzo = 1 if nzo == "Да" else 0
X_amk = 1 if amk == "Да" else 0

# --- Расчет при нажатии кнопки ---
if st.button("Рассчитать вероятность"):
    
    Z = (
        -2.8
        - 1.27 * X_rody
        + 1.57 * X_dlit
        + 0.72 * X_nzo
        + 1.06 * X_amk
        - 0.09 * vozrast
        - 0.3 * razmer
    )
    
    P = (1 / (1 + math.exp(-Z))) * 100

    st.markdown("### ✅ Результат:")
    st.metric("Вероятность рецидива (%)", f"{P:.2f}")

    # Интерпретация риска
    if P < 30:
        st.success("Низкий риск рецидива")
    elif 30 <= P < 60:
        st.warning("Умеренный риск рецидива")
    else:
        st.error("Высокий риск рецидива")

st.markdown("---")
st.caption("Модель носит исследовательский характер и не заменяет клиническое решение врача.")
