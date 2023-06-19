#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!pip install pyttsx3

import pyttsx3
import os
import time
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
# Arquivo
arquivo = open("frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
engine.say(conteudo)
engine.runAndWait()
arquivo.close()


# In[ ]:


# Instalar o Arquivo .EXE
#!pip install pyinstaller


# In[ ]:


# Criar o Arquivo Executavel via Linha de Comando vozTexto.EXE
#pyinstaller --onefile "vozTexto.py"

