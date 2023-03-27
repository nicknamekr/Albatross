from flask import Flask, render_template, send_from_directory, request, redirect
import openai, os
import wikipedia

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
  print(response)
  return render_template('search.html', genie_ai_body = response.choices[0].message.content)

@app.route('/search.li')
def search_li():
  return render_template('search.html', genie_ai_body = "For now, lightning search doesn't support Genie AI Search.")

@app.route('/geniepaint')
def geniepaint():
  return render_template('geniepaint.html')

@app.route('/geniepaint.dl')
def geniepaint_dl():
  response = openai.Image.create(
    prompt=request.args.get('q'),
    n=1,
    size="512x512"
  )
  image_url = response['data'][0]['url']
  return '''
  <head>
   <title>downloader</title>
  </head>
  <body>
   <div style="display: none;"><span>AI PAINTER</span></div>
    <script>
      function downloadURI(uri, name){
          var link = document.createElement("a");
          link.setAttribute("download", name);
          link.href = uri;
          document.body.appendChild(link);
          link.click();
          link.remove();
      }
      downloadURI("image_url", "geniepainter-ai-result.png"); 
    </script>
  </body>
  '''.replace('image_url', image_url)

@app.route('/pagos.idx')
def pagos_idx():
  wikipedia.set_lang("ko")
  x = wikipedia.summary(request.args.get('q', '위키백과:대문'))
  print(x)
  return render_template('pagos.html', pgv = x)

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
