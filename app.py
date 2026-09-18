
import streamlit as st
from langchain_ollama import ChatOllama

st.set_page_config(page_title='ChatBot',page_icon='💬')
st.title('*ChatBot*')
st.caption('*AI-InterViewer*')
chat = ChatOllama(model='llama3.2',temperature=0)
if 'setup' not in st.session_state:
    st.session_state.setup = False
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = False
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'chat_complete' not in st.session_state:
    st.session_state.chat_complete = False


def _setup():
    st.session_state.setup = True
def _feedback():
    st.session_state.feedback = True

if not st.session_state.setup:
    st.header('Profile & Info',divider='blue')
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if 'experience' not in st.session_state:
        st.session_state['experience'] = ''
    if 'skills' not in st.session_state:
        st.session_state['skills'] = ''
    st.session_state['name'] = st.text_input(label='Name',value = st.session_state['name'],max_chars=None,placeholder='Enter your Name')
    st.session_state['experience']= st.text_area(label='Experience',value = st.session_state['experience'],max_chars=None,placeholder='Share your Experience')
    st.session_state['skills'] = st.text_area(label='Skills',max_chars=None,value = st.session_state['skills'],placeholder=' List Out your Skills')


    st.write(f'*Name* : {st.session_state['name']}')
    st.write(f'*Experience* : {st.session_state['experience']}')
    st.write(f'*Skills* : {st.session_state['skills']}')

    st.subheader('Company & Position',divider='blue')
    if 'level' not in st.session_state:
        st.session_state['level'] = 'Junior'
    if 'position' not in st.session_state:
        st.session_state['position'] = 'ML-Engineer'
    if 'company' not in st.session_state:
        st.session_state['company'] = 'Amazon'
    col1,col2 = st.columns(2)
    with col1:
        st.session_state['level'] = st.radio(
            '*Choose Level*',options=['Junior','Mid-Level','Senior']
        )
    with col2:
        st.session_state['position'] = st.selectbox(
            '*Choose Position*',('ML-Engineer','AI-Engineer','Data-Engineer')
        )
    st.session_state['company'] = st.selectbox(
        '*Select Company*',('Amazon','Meta','Google','Spotify')
    )
    st.write(f'*Your Info* : {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}')
    if st.button('Start Interview',on_click=_setup):
        st.write('Complete setup ,Starting Interview')

if st.session_state.setup and not st.session_state.feedback and not st.session_state.chat_complete:
    st.info(
        '''Start by Introducing yourself''',
        icon = '🤝'
    )
    if not st.session_state.messages:
        st.session_state['messages'] = [
            {
                'role':'system',
                'content':f'''you're a HR Executive that interviews an interviewee called {st.session_state['name']} with experience
                {st.session_state['experience']} and skills {st.session_state['skills']}.
                you should interview the candidate for the postion {st.session_state['level']} {st.session_state['position']} at the company '''
            }
        ]
    for message in st.session_state.messages:
        if message['role'] != 'system':
            with st.chat_message(message['role']):
                st.markdown(message['content'])
    if st.session_state.count < 5:
        if prompt := st.chat_input('Type your message',max_chars=None):
            st.session_state.messages.append({'role':'user','content':prompt})
            with st.chat_message('user'):
                st.markdown(prompt)
            if st.session_state.count < 4:
                with st.chat_message('assistant'):
                    messages = [
                        {
                            'role':m['role'],
                            'content':m['content']
                        } for m in st.session_state.messages
                    ]
                    stream = chat.stream(messages)
                    def chatStream():
                        for i in stream:
                            yield i.content
                    response = st.write_stream(chatStream())
                st.session_state.messages.append({'role':'assistant','content':response})
            st.session_state.count += 1
    if st.session_state.count >= 5:
        st.session_state.chat_complete = True
if st.session_state.chat_complete and not st.session_state.feedback:
    if st.button('Get FeedBack',on_click=_feedback):
        st.write('Fetching FeedBack')