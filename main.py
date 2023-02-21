from flask import Flask

import datetime

app = Flask(__name__, static_url_path="/static")
app= Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  page1=f"""<html><body>
  <p><a href = "/portfolio">My Portfolio</a></p>
  </body>
  </html>
  <html><body>
  <p><a href = "/linktree">Link Tree</a></p>
  </body>
  </html>"""

  return page1



  
  
  
@app.route('/linktree')
def home():
  now=datetime.datetime.now()
  page2 = f"""
  
  <html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/styles.css" rel="stylesheet" type="text/css" />
</head>

<body>

   
    <div class="me">  
  <h1>Meet me...Kiprono Bett Collins</h1>
    </div>

<div class="grid">
<div class="left"> </div> 
<div class="right"> </div>
  </div>
    
    <div class="pninja">  
      <img src=static/img/ninja.PNG width=200 height="150">
    </div>
  
      <div class = "intro" > 
      <p>
        Here is a representation of my life's digital  contributions...not all but my valued ones! Welcome for a fly-by in my world pal...
      </p>
        </div> 
  
  
  
    <p class="gitp"> 
      View my repositories and my code from Github 
    </p>

     <div class= "git">
    <p>
      <a href= "https://github.com/texsavi" >
      <div>
        <img src=static/img/gith.png width=50>
      </div>
    </div>    
      </a>
    </p>

      <div class="gitwrd" >
    <p >
      <a href= https://github.com/texsavi> 
        @Github
      </a>
    </p>
    </div>

     <div class="gitwrd" >
    <p> 
      I love sharing my ideas and building with the public via twitter 
    </p>
     </div>

    <div class= "twitter"> 
    <p>
      <a href="https://twitter.com/_kipronobett">
        <div>
          <img src=static/img/twitter.png width=50>
        </div>  
      </a>
    </p>
    </div>
  
    <p class="twitwrd">
      <a href= https://twitter.com/_kipronobett> 
        @_kipronobett
      </a>
    </p>
  
    <p <div class="replp"> 
      My journey in software development began at Replit with 100 Days of Python challenge. Ever since, I build remotely and share my works at Replit.  </div>     </p>

          <div  class= "replit">
    <p>
      <a href="https://replit.com/@bettech"> 

          <img src=static/img/repl.PNG width=50>
        </div>  
      </a>
    </p>
  
    <p class="replwrd">
      <a href= https://github.com/texsavi> 
        @bettech
      </a>
    </p>
  
    <p class="linkp"> 
      Here is my LinkedIn profile. Let's connect professionally and collaborate in building. 
    </p>

     <div class= "linkedin">
    <p>
      <a href="https://www.linkedin.com/in/collins-bett-kiprono">
        
          <img src=static/img/linkin.png width=50>
        </div> 
      </a>
    </p>

    <p class="linkwrd">
      <a href= https://github.com/texsavi> 
        @collinsbett
      </a>
    </p>
  
    <p class="medp"> 
      I periodically contribute on Medium by writing STEM blogs. Mainly technical articles on Electrical Engineering and technology and Software development. 
    </p> 

  <div class= "medium">
    <p>
      <a href="https://medium/@colebett33">
        
          <img src=static/img/medium.png width=50>
        </div> 
      </a>
    </p>  
  
    <p class="medwrd">
      <a href= https://medium/@colebett33> 
        colebett33@medium.com
      </a>
    </p>  

  <p class="email">
     *******{now}*********
    </p> 
 <p class="mail">  <img src=static/img/gm.png width=18 height=20> 
   <a href= https://mail.google.com/@colebett33> 
        colebett33@gmail.com
      </a>
 </p> 
  <script src="script.js"></script>

 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="yellow" defer></script> 
</body>

</html>

  """
  return page2
  
@app.route('/portfolio') 
def pagee():
  page=f"""
  <html>

  <head>
    <title>My Code My Call</title>
  </head>
  <link href="static/style.css" rel="stylesheet" type="text/css" />
  <body>
    <h1>My Portfolio: Kiprono Bett  </h1>

  <div>
   <img src=static/img/myP.PNG width=500 alt="colorful image titled portfolio"/>
  </div>
    
    
    <p class="intro">This one here is mainly a representation of my life's work. A representation of my digital contributions that I am really passionate about. You are free to explore, inquire more and share. Inquiry invites progress through innovation. I explore, inquire, learn, build and share.</p>
    <h2>Here I tell you more about myself</h2>
    <p class="intro">My interests, skills and projects that you would love to be part of or contribute in are SHARED HERE</p>
    <h3>My skills are listed here </h3>
    <ul>
      <li>Critical thinking</li>
      <li>Time Management</li>
      <li>Effective Communication</li>
      <li>Team work</li>
      <li>Python</li>
      <li>HTML</li>
      <li>Accurate ChatGPT Prompting</li>
      <li>Design Thinking</li>
      <li>Product development</li>
    </ul>  
      
          
  
    <h4>Interesting, isn't it? Scroll by and <a href="moreportfolio.html">view more
       
      </a> pal 
    </h4>
  
    <h4>
      Ping me for a practical guide of me working
    </h4>
    
    <p class="ping">
      You know what? Just
      <a href="moreportfolio.html">Explore Here</a> 
       instead of pinging me friend
    </p>
                                                                      
    <h5>
      For my service delivery 
      <a href="https://github.com/texsavi?tab=repositories">
        WELCOME HERE
      </a>
    </h5>
    
    <h6>
      This is the smallest screen writing I could get--but we can do less.
    </h6>
    
    <p class= "bye">
      Bye for now friend! Not the least though! More coming ahead soon!
    </p>
    
  </body>
  
</html>
  
  """
  return page



app.run(host='0.0.0.0', port=81)