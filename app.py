#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import speech_recognition as sr


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        file = request.files['file']
        print("File Received")
        filename = secure_filename(file.filename)
        file.save("static/" + filename)
        a = sr.AudioFile("static/" + filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="No file."))
    
if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




