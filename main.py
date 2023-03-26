from flask import Flask, render_template, send_from_directory, request, redirect
import openai, os

app = Flask('app')
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/search.w')
def search():
  response= openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": request.args.get('q')}]
  )
  # response = openai.Completion.create(
  #   model="text-davinci-003",
  #   prompt= request.args.get('q'),
  #   temperature=0.65,
  #   max_tokens=500,
  #   stop=[" Human:", " AI:"]
  # )
  print(response)
  return render_template('search.html', genie_ai_body = response.choices[0].message.content)

@app.route('/chat.shorten')
def chat_linking():
  return redirect('https://albatross-ai.vercel.app/', code = '302')

@app.route('/ping.uptimerobot')
def ping_for_uptimerobot():
  return '.'

@app.route('/logo.svg')
def logo():
    return send_from_directory(app.static_folder, request.path[1:])

app.run(host='0.0.0.0', port=5523, debug=True)
