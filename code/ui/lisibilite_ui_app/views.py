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

	def setOutputValuesToSession(self, request, outputModel):
		coreMetrics = outputModel.coreMetrics
		readabilityMetrics = outputModel.readabilityMetrics
		# Text Category and Description
		request.session['textCategory'] = outputModel.getCategory()
		request.session['textPurpose'] = outputModel.getDescription()
		# Core Metrics
		request.session['totalWords'] = coreMetrics.getTotalWords()
		request.session['totalSentences'] = coreMetrics.getTotalSentences()
		request.session['totalHardWords'] = coreMetrics.getTotalComplexWords()
		request.session['totalEasyWords'] = coreMetrics.getTotalEasyWords()
		request.session['totalSyllables'] = coreMetrics.getTotalSyllables()
		request.session['totalCharacters'] = coreMetrics.getTotalCharacters()
		# Readability Metrics
		request.session['fresValue'] = readabilityMetrics.getFRES().roundedValue
		request.session['fresLabel'] = readabilityMetrics.getFRES().label
		request.session['fkglValue'] = readabilityMetrics.getFKGL().roundedValue
		request.session['fkglLabel'] = readabilityMetrics.getFKGL().label
		request.session['gfiValue'] = readabilityMetrics.getGFI().roundedValue
		request.session['gfiLabel'] = readabilityMetrics.getGFI().label
		request.session['ariValue'] = readabilityMetrics.getARI().roundedValue
		request.session['ariLabel'] = readabilityMetrics.getARI().label
		request.session['smogValue'] = readabilityMetrics.getSMOG().roundedValue
		request.session['smogLabel'] = readabilityMetrics.getSMOG().label
		request.session['cliValue'] = readabilityMetrics.getCLI().roundedValue
		request.session['cliLabel'] = readabilityMetrics.getCLI().label
		request.session['lwsValue'] = readabilityMetrics.getLWS().roundedValue
		request.session['lwsLabel'] = readabilityMetrics.getLWS().label
		request.session['fryValue'] = readabilityMetrics.getFRY().roundedValue
		request.session['fryLabel'] = readabilityMetrics.getFRY().label

	def post(self, request):
		contentString = request.POST.get('text_content', None)
		if contentString is not None:
			outputModel = Lisibilite(contents=contentString).outputModel
			if outputModel is not None:
				self.setOutputValuesToSession(request, outputModel)
		else:
			outputModel = None
		return redirect('displayscores')


class DisplayScoresPageView(View):

	def generateMetricsDict(self, request):
		metricsDict = {}
		for key in request.session.keys():
			metricsDict[key] = request.session.get(key)
		return metricsDict

	def get(self, request):
		metricsDict = self.generateMetricsDict(request)
		return render(request, 'displayscorespage.html', metricsDict)

	def post(self, request):
		return render(request, 'displayscorespage.html')
