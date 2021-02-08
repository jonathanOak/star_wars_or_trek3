import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict(message):
    
    model=load_model('stars15.h5')
    with open('tokenizer.pickle', 'rb') as handle:
        
        tokenizer = pickle.load(handle)
        x_1 = tokenizer.texts_to_sequences([message])
        x_1 = pad_sequences(x_1, maxlen=500)
        predictions = model.predict(x_1)[0][0]
    return predictions


title_ = '''

  <h2> </h2>
  <h2> </h2>
  <h2> </h2>
  <h2> </h2>

'''

st.markdown(title_, unsafe_allow_html=True)
#st.title('we will put something here')
message = st.text_area('','Beam your Star Wars or Star Trek phrase down here and find out who your father is ...')

if st.button('Analyze'):
    with st.spinner('Analyzing the text …'):
        prediction = predict(message)
    
    if prediction > 0.6:
        st.warning(' Belongs to **Star Wars** with **{:.2f}%** confidence'.format(prediction*100))
        st.success('I find your lack of faith disturbing')
        st.balloons()
    elif prediction < 0.4:
        st.warning('Belongs to **Star Trek** with **{:.2f}%** confidence'.format((1-prediction)*100))
        st.success('In critical moments, men sometimes see exactly what they wish to see')
        st.balloons()
    else:
        st.warning('Not sure! Try to add some more words')
        st.success('Insufficient facts always invite danger')

page_bg_img = '''
<style>
body {
background-image: url("https://netivist.org/uploads/forum/discussions/pictures/5372277155f4f50bfc8449f4/star-wars-vs-star-trek.jpg");
background-size: cover;
}
</style>
'''


st.markdown(page_bg_img, unsafe_allow_html=True)