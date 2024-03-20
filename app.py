import streamlit as st
import requests
import time
import json


st.title('Monthly Business Review')
txt = st.text_area('Business Summary', value="")
vague_data = st.checkbox('Do not use any vague data.')
vague_expression = st.checkbox('Provide alternatives to any Numerically vague expressions such as multiple, and various etc.')
common_acronym = st.checkbox('Do not spell out common acronyms.')
lower_case = st.checkbox('use lowercase for nouns and noun phrases that are not proper nouns.')
long_sents = st.checkbox('Rephrase the sentenses longer than 25 words.')

def rules():
    rules = ''
    if vague_data:
         rules = '<rule>Do not use any vague data.</rule>'
    if vague_expression:
        rules += '<rule>Provide alternatives to any Numerically vague expressions such as multiple, and various etc.</rule>'
    if common_acronym:
        rules += '<rule>Do not spell out common acronyms.</rules>'
    if lower_case:
        rules += '<rule>use lowercase for nouns and noun phrases that are not proper nouns.</rule>'
    if long_sents:
        rules += '<rule>Rephrase the sentenses longer than 25 words.</rule>'
    ##st.write(rules)
    return rules


def calling_api():
    with st.spinner('analyzing...'):
        ##time.sleep(5)
        url = "https://qgux9ug2s3.execute-api.us-east-1.amazonaws.com/bedrock-stage/"
        my_request = {'text': txt, 'rules': rules()}
        response = requests.post(url, json=my_request)
        data = response.json()['body']
        summary = json.loads(data)
    st.success(summary['completion']) 
         

if st.button('Submit'):
    calling_api()

def lambda_handler(event, context):
        print(event)
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
     }
