from django.shortcuts import render
from django.http import HttpResponse
import re
def index(request):
	return render(request,'index.html')

def analyze(request):
	djtext = request.POST.get("text","default")
	removepunc = request.POST.get("removepunc","off")
	fullcaps = request.POST.get("fullcaps","off")
	newlineremover = request.POST.get("newlineremover","off")
	extraspaceremove = request.POST.get("extraspaceremove","off")
	
	if removepunc == 'on':
		allpuncs = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
		inital_text = ""
		for char in djtext:
			if char not in allpuncs:
				inital_text = inital_text + char
		params = {"inital_text":inital_text,"purpose":"Puntuations Removed"}
		djtext = inital_text
				
	if fullcaps == 'on':
		inital_text = ""
		for char in djtext:
			inital_text = inital_text + char.upper()
		params = {"inital_text":inital_text,"purpose":"Capitalized"}
		djtext = inital_text	

	if newlineremover == 'on':
		# inital_text = ""
		# for char in djtext:
			# if char != "\n" and char != "\r":
				# inital_text = inital_text + char	
		inital_text = djtext.replace('\r', '').replace('\n', ' ')
		params = {"inital_text":inital_text,"purpose":"New Lines Removed"}
		djtext = inital_text

	if extraspaceremove == 'on':
		inital_text = ""
		for index,char in enumerate(djtext):
			if not (djtext[index] == " " and djtext[index+1] == " "):
				inital_text = inital_text + char			
		params = {"inital_text":inital_text,"purpose":"Extra Space Removed"}
		djtext = inital_text
		
	if removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off' and extraspaceremove == 'off':
		params = {
					"inital_text":"You didn't select any option",
					"error":"Text couldn't analyzed!"}
		
	return render(request,'analyze.html',params)					
		
		
