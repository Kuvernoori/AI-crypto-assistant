import streamlit as st
import requests
import ollama

# Функция для получения информации из Coingecko
def get_crypto_info(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Генерация ответа через Llama3
def generate_response(prompt):
    result = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": "Ты эксперт по криптовалютам."},
            {"role": "user", "content": prompt}
        ]
    )
    return result['message']['content']

# Интерфейс
st.title("🧠 AI Crypto Assistant")
coin_name = st.text_input("Введите название криптовалюты (например, bitcoin):")

if coin_name:
    with st.spinner("Получение данных..."):
        data = get_crypto_info(coin_name)
        if data:
            name = data['name']
            price = data['market_data']['current_price']['usd']
            market_cap = data['market_data']['market_cap']['usd']

            prompt = (
                f"{name} (цена: ${price}, капитализация: ${market_cap}) — "
                f"напиши краткий обзор для новичков в криптовалютах."
            )

            st.success("Информация получена!")
            st.subheader("Ответ AI:")
            response = generate_response(prompt)
            st.write(response)

            # Показ JSON (по желанию)
            with st.expander("📦 JSON-ответ от Coingecko"):
                st.json(data)
        else:
            st.error("Криптовалюта не найдена.")
