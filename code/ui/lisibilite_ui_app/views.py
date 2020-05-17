from django.shortcuts import render, redirect
from django.views import View
from lisibilite.Lisibilite import Lisibilite


class HomePageView(View):
	def get(self, request):
		return render(request, 'homepage.html')

	def post(self, request):
		return None


class UserInputPageView(View):
	def get(self, request):
		return render(request, 'userinputpage.html')

	def post(self, request):
		contentString = request.POST.get('text_content', None)
		if contentString is not None:
			readabilityMetrics = Lisibilite(contents=contentString).metrics
		else:
			readabilityMetrics = None

		if readabilityMetrics is None:
			readabilityMetrics = "I am sorry, I am empty now, because no text was provided!"

		request.session['textCategory'] = request.POST.get('text_category', None)
		request.session['textPurpose'] = request.POST.get('text_purpose', None)
		request.session['totalWords'] = readabilityMetrics.getTotalWords()
		request.session['totalSentences'] = readabilityMetrics.getTotalSentences()
		request.session['totalHardWords'] = readabilityMetrics.getTotalComplexWords()
		request.session['totalEasyWords'] = readabilityMetrics.getTotalEasyWords()
		request.session['totalSyllables'] = readabilityMetrics.getTotalSyllables()
		request.session['totalCharacters'] = readabilityMetrics.getTotalCharacters()
		return redirect('displayscores')


class DisplayScoresPageView(View):
	def __init__(self):
		self.metricsDict = {}

	def get(self, request):
		# metricsDict = {}
		self.metricsDict['textCategory'] = request.session.get('textCategory')
		self.metricsDict['textPurpose'] = request.session.get('textPurpose')
		self.metricsDict['totalWords'] = request.session.get('totalWords')
		self.metricsDict['totalSentences'] = request.session.get('totalSentences')
		self.metricsDict['totalHardWords'] = request.session.get('totalHardWords')
		self.metricsDict['totalEasyWords'] = request.session.get('totalEasyWords')
		self.metricsDict['totalSyllables'] = request.session.get('totalSyllables')
		self.metricsDict['totalCharacters'] = request.session.get('totalCharacters')
		return render(request, 'displayscorespage.html',
			self.metricsDict)

	def post(self, request):
		return render(request, 'displayscorespage.html')
