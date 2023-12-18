import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.title('Pinguim de Palmer')
st.markdown('Use this Streamlit app to make your own...')

selected_species = st.selectbox('Quais especies vocês gostariam de visualizar?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('x axis',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('y axis',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_gender = st.selectbox('Gender?',['Male','Female'])


penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')
#if penguin_file is not None:
#   penguins_df = pd.read_csv(penguin_file)
#else:
#    st.write('Você não carregou nenhum arquivo')
#    st.stop()

#penguins_df = penguins_df[penguins_df['species'] == selected_species]
@st.cache()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        st.write('Vc não carregou')
        st.stop()
    return(df)
penguins_df = load_file(penguin_file)

if (selected_gender == 'Male'):
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
else:
    penguins_df = penguins_df[penguins_df['sex'] == 'female']

#st.write(penguins_df.groupby('species').count())

#st.write(penguins_df.head())
sns.set_style('darkgrid')
#markers = {"Adelie": "X", "Gentoo":"s", "Chinstrap":"o"}
markers = {"male": "X", "female":"s"}
fig, ax = plt.subplots()
#ax = sns.scatterplot(x = penguins_df[selected_x_var],y = penguins_df[selected_y_var])
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, y = selected_y_var, hue = 'species'
                     , size = 'body_mass_g', sizes=(10,150))
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Scatterplot of {} Penguins'.format(selected_gender))
st.pyplot(fig)