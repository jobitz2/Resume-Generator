from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''

    if request.method == 'POST':
        resume_text = request.form['resume_text']
        job_description = request.form['job_description']

        prompt = f'''
You are a professional career assistant.

Given the resume text and job description below, do the following:
1. Write 3 stronger resume bullet points tailored to the job.
2. Write a short professional cover letter.

Resume:
{resume_text}

Job Description:
{job_description}
'''

        response = client.responses.create(
            model='gpt-5',
            input=prompt
        )

        result = response.output_text

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)