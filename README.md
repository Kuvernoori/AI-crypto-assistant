🧠 AI Crypto Assistant

📌 Project Objective
The goal of this project is to build an AI assistant that provides users with detailed information about cryptocurrencies. It combines real-time data from the CoinGecko API with natural language generation from a local Llama3 model via Ollama.

🛠 Technologies Used
- Python

- Streamlit – Web UI framework

- Ollama + Llama3 – Local language model for natural responses

- CoinGecko API – Public cryptocurrency data

🛠 Python libraries:
- requests
- streamlit
- ollama

📁 Project Structure
```
ai-crypto-assistant/
├── app.py               
├── requirements.txt     
├── README.md            
├── screenshots/        
│   ├── ui.png
│   ├── json_response.png
│   └── terminal.png
```


🚀 How to Run
1. Install Python (if not already installed)
Make sure you have Python 3.10+:
```
python --version
```
3. Install Ollama and run Llama3
```ollama run llama3```
This will download and start the Llama3 model locally.

4. Clone the project or create a working directory
```git clone https://github.com/yourusername/ai-crypto-assistant.git```
```cd ai-crypto-assistant```
5. Install dependencies
```pip install -r requirements.txt```
6. Run the application
```python -m streamlit run app.py```
This will launch a web interface at http://localhost:8501.



