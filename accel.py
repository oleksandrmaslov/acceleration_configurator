import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Заголовок приложения
st.title("Pointer Acceleration Tool")

# Боковая панель с настройками
st.sidebar.header("Acceleration settings")
min_factor_val = st.sidebar.slider("min-factor (0.1× – 1.0×)", 100, 1000, 500, step=10)
max_factor_val = st.sidebar.slider("max-factor (1.0× – 10.0×)", 1000, 10000, 4000, step=10)
speed_threshold = st.sidebar.slider("speed-threshold (counts/sec)", 100, 5000, 800, step=10)
speed_max = st.sidebar.slider("speed-max (counts/sec)", 1000, 10000, 4000, step=10)
accel_exponent = st.sidebar.slider("acceleration-exponent", 1, 5, 2, step=1)

# Гарантируем, что порог не больше максимальной скорости
if speed_threshold > speed_max:
    speed_threshold = speed_max

# Переводим значения коэффициентов в вещественные (1000 -> 1.0×)
min_factor_float = min_factor_val / 1000.0
max_factor_float = max_factor_val / 1000.0

# Определяем функцию расчёта коэффициента ускорения
def accel_factor(v):
    if v < speed_threshold:
        return min_factor_float
    elif v > speed_max:
        return max_factor_float
    else:
        norm = (v - speed_threshold) / (speed_max - speed_threshold)
        return min_factor_float + (max_factor_float - min_factor_float) * (norm ** accel_exponent)

# Генерируем массив значений скорости (от 0 до чуть больше speed_max)
speeds = np.linspace(0, speed_max * 1.1, 300)
# Рассчитываем коэффициенты ускорения для каждой скорости
vectorized_accel = np.vectorize(accel_factor)
factors = vectorized_accel(speeds)

# Создаём график с помощью Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=speeds, y=factors, mode="lines", name="Acceleration Factor"))
fig.update_layout(
    xaxis_title="Speed (counts/sec)",
    yaxis_title="Acceleration Factor (×)",
    showlegend=False
)
st.plotly_chart(fig, use_container_width=True)

# Генерируем текст конфигурации DTS
config_text = f"""&pointer_accel {{
    input-type = <INPUT_EV_REL>;
    track-remainders;
    min-factor = <{min_factor_val}>;
    max-factor = <{max_factor_val}>;
    speed-threshold = <{speed_threshold}>;
    speed-max = <{speed_max}>;
    acceleration-exponent = <{accel_exponent}>;
}};"""

st.subheader("Configuration DTS")
st.code(config_text, language="dts")

# Дополнительно можно вывести текстовое поле для копирования (в st.code уже встроена кнопка копирования)
st.text_area("Config DTS (for copying)", config_text, height=150)
