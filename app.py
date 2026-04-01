import streamlit as st
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
model=load_model('next_word_lstm.h5')
import pickle

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
def predict_next_word(model, tokenizer, text, max_sequence_len):
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np

    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')

    predicted = model.predict(token_list, verbose=0)
    predicted_index = np.argmax(predicted, axis=1)[0]

    # Reverse mapping
    index_word = {index: word for word, index in tokenizer.word_index.items()}

    return index_word.get(predicted_index, "Not Found")
st.title('Next word prediction with LSTM ')
input_text=st.text_input("enter the sequence of words", "To be or not to be")
if st.button("predict next word"):
    max_sequence_len = model.input_shape[1] + 1
    next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)

    st.write(f"Next word: {next_word}")
    st.write("DEBUG:", next_word)