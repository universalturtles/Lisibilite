from django.shortcuts import render, redirect
from django.views import View
from lisibilite.Lisibilite import Lisibilite


class HomePageView(View):

	def get(self, request):
		"""
		The function to handle the HTTP GET request for home page.
		:param request: The django HTTP request object
		:return The render object
		"""
		return render(request, 'homepage.html')

	def post(self, request):
		"""
		The function to handle the HTTP POST request for Home Page.
		:param request: The django HTTP request object
		:return None
		"""
		return None


class UserInputPageView(View):

	def get(self, request):
		"""
		The function to handle the HTTP GET request for text input page.
		:param request: The django HTTP request object
		:return The render object
		"""
		return render(request, 'userinputpage.html')

	def setOutputValuesToSession(self, request, outputModel):
		"""
		The function to set the data from output model as session variables.
		:param request: The django HTTP request object
		:param outputModel: The lisibilite output model
		:return None
		"""
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
		"""
		The function to handle the HTTP POST request for text input page.
		:param request: The django HTTP request object
		:return The redirect object
		"""
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
		"""
		The function to retreive the output metrics from the session object.
		:param request: The django HTTP request object
		:return The dictionary object containing the metrics.
		"""
		metricsDict = {}
		for key in request.session.keys():
			metricsDict[key] = request.session.get(key)
		return metricsDict

	def get(self, request):
		"""
		The function to handle the HTTP GET request for metrics display.
		:param request: The django HTTP request object
		:return The render object
		"""
		metricsDict = self.generateMetricsDict(request)
		return render(request, 'displayscorespage.html', metricsDict)

	def post(self, request):
		"""
		The function to handle the HTTP POST request for metrics display.
		:param request: The django HTTP request object
		:return The render object
		"""
		return render(request, 'displayscorespage.html')
