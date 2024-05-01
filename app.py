import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

st.set_page_config(page_icon='🤖',
                   page_title="Blog Generator",                  
)

##Function to get response from LLama2 model (Backend)

def response(input_text,no_words,blog_style):

    #calling Llama2
    llm=CTransformers(model='model\llama-2-7b-chat.Q2_K.gguf',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    

    #Prompt Template
    prompt=PromptTemplate(input_variables=['blog_style','input_text','no_words'],template='Write a blog for {blog_style} audience on the topic {input_text} under {no_words} words or less.')

    ## Generate the response from Llama2 
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return(response)


## Streamlit Code (Frontend)

st.header('Generate Blogs 🤖')

input_text=st.text_input("Enter the Blog Topic")

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('Enter number of words')
with col2:
    blog_style=st.selectbox('Writing the blog for ______  audience',('Beginner','Intermediate','Pro'))

submit=st.button('Generate')


# Final Response
if submit:
    st.write(response(input_text,no_words,blog_style))

