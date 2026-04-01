# 🔮 Next Word Prediction using LSTM

🚀 Live App:https://word-prediction-using-lstm-2g85e4leglehgmzjuaeb5s.streamlit.app/

---

## 📌 Project Overview

This project builds a **Next Word Prediction system** using a **Deep Learning LSTM (Long Short-Term Memory)** model.

Given a sequence of words, the model predicts the most probable next word based on learned language patterns.

---

## 🎯 Features

✨ Predict next word from user input
✨ Built using LSTM neural networks
✨ Trained on text dataset (Hamlet)
✨ Interactive web app using Streamlit
✨ Deployed on Streamlit Cloud

---

## 🧠 How it Works

1. Text data is preprocessed and tokenized
2. Sequences are generated for training
3. LSTM model learns word patterns
4. Given input text → model predicts next word

---

## 🛠️ Tech Stack

* Python 🐍
* TensorFlow / Keras 🤖
* NumPy 📊
* Streamlit 🌐

---

## 📂 Project Structure

```
├── app.py                  # Streamlit app
├── experiments.ipynb      # Model training notebook
├── tokenizer.pickle       # Saved tokenizer
├── next_word_lstm.h5      # Trained model
├── hamlet.txt             # Dataset
├── requirements.txt       # Dependencies
├── runtime.txt            # Python version
├── .gitignore
```

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/divyasreevemula918/word-prediction-using-LSTM.git
cd word-prediction-using-LSTM
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 🌐 Deployment

This app is deployed using **Streamlit Cloud**

🔗 Live Demo:
👉 https://word-prediction-using-lstm-2g85e4leglehgmzjuaeb5s.streamlit.app/

---

## 📸 Screenshots

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7bdeb032-7c60-4c33-aef2-15c773b826fb" />


---

## 🚧 Limitations

* Model trained on limited dataset
* Predictions may not always be accurate
* Old English text (Shakespeare style)

---

## 🚀 Future Improvements

* Use larger dataset (Wikipedia / books)
* Add top-5 predictions
* Generate full sentences
* Improve UI/UX

---

## 👩‍💻 Author

**Divya Sree Vemula**
🔗 GitHub: https://github.com/divyasreevemula918


