import streamlit as st

# Title/text
st.title('This is Streamlit.......')

# Header
st.header('This is a Header.......')

# subheader
st.subheader('This is a subheader.........')

# normal text
st.text('This is a normal text.......')

# markdown
st.markdown('# This is a markdown....') # the number of #(hashtags) matter

# enter colorful text
st.success('Success......')

st.info('Information....')

st.warning('This is a warning.....')

st.error('This is an error.....')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

# Get Help about python
st.help(range)

# writing text
st.write('Text with write........')

a = range(0,10)
st.write(a)

# widget
#1) checkbox
if st.checkbox('Show/Hide'):
    st.text('Showing or Hiding')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

#2) radio
status = st.radio('What is your status', ('Active', 'Inactivee'))
if status == 'Active':
    st.success('You are Active...')
else:
    st.warning('Please, Activate....')


# selectbox
occupation = st.selectbox("Your occupation", ['Programmer', 'Data Scientist', 'Doctor'])
st.write('Your selected occupation is: ', occupation)

# multiselect
location = st.multiselect('Where do you work?', ('London', 'New York', 'califonia', 'kiev', 'Nepal'))
st.write('You selected', len(location), 'locations: that is', location)

# slider
level = st.slider('What is your level',10,100)

# buttons
if st.button('About'):
    st.text('Streamlit is Cool')

# receive text input
first_name = st.text_input('Enter Your First Name', 'Type Here.......')
if st.button('Submit'):
    result = first_name.title()
    st.success(result)

# text area
message = st.text_area('Enter Your Message', 'Type Here.......')
if st.button('Click Here'):
    result = message.title()
    st.success(result)

# date input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

# time input
time = st.time_input('The time is', datetime.time())

# displaying JSON
st.text('Displaying JSON')
st.json({
    'name':'Jesse',
    'gender':'male'
})

# display raw code - method 1
st.text('display raw code')
st.code('import numpy as np')

# display raw code - method 2
with st.echo():
    # this is a comment
    import pandas as pd
    df = pd.DataFrame()
    df.head()
    df.tail()


# progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+3)


# spinner
with st.spinner('loading.....'):
    time.sleep(5)
st.success('Finished....')

# balloons
st.balloons()

# sidebar
st.sidebar.header('About')
st.sidebar.text('Streamlit tutorial')

# functions
@st.cache
def run_fxn():
    return range(100)
st.write(run_fxn())

# plot
st.pyplot()

# dataframe
st.dataframe(df)

