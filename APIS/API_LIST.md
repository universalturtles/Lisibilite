# List of APIs

- Readability Metrics
- Generate API Token
- User Add
- User Delete
- User Update

## Future
- Sentiment
- Magnitude of Emotion
- Keyword Density Analysis
- ...

# General Response Codes

| Status Code | Description |
| ----------- | ----------- |
|400|Bad Request|
|401|Unathorized|
|403|Forbidden|
|404|Resource Not Found|
|500|Internal Server Error|
|503|Service Unavailable|

# Readability Metrics
**REQUEST**
```
POST /api/v1/readability 
or
POST /api/latest/readability
```

**URL Params**
```
fields=*[default] | [readability_metrics,text_metrics]
```

**Headers**
```
Content-Type: application/json, application/json+hal, application/xml
Authorization: Bearer <Token>, Basic <base64(username:token)>, Basic <encrypted(base64(username:password))>
```

**Request Body**
```
{
	"text": "<Plain Text : limit below>",
	"category": [SCIENTIFIC, GENERAL, WEB, ESSAY, OTHER....], 
	"purpose": "[RESEARCH, BLOG, JOURNAL, CONTENT_PAGES, MEMO, EMAIL, DESIGN_DOC,....]"
}
```

**Response Body**
```
{
	"_links": {
    "self": {
      "href": "/readability/<$document_id>"
    },
    "document_category": "<category from ENUM>",
    "document_purpose": "<purpose from ENUM>"
	"document_id": "<uuid>",
	"readability_metrics": {
		"fres": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"fkgl": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"gfi": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"ari": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"smog": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"cli": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"lws": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"fry": {
			"score":00,
			"desc":"<Description of the score>"
		},
		"lisibilite_score": {
			"score":00,
			"desc":"<Description of the score>"
		}
		"_links": {
    		"self": {
      			"href": "/readability/readability_metrics/<$document_id>"
   			 }
		}
	},
	"text_metrics": {
		"average_sentence_length": 00,
		"average_word_length": 00,
		"total_sentences": 00,
		"total_words": 00,
		"total_paragraphs": 00,
		"total_misspelled": 00,
		"_links": {
    		"self": {
      			"href": "/readability/text_metrics/<$document_id>"
   			 }
		}
	},
	"versions":{
		"_links": {
    		"self": {
      			"href": "/readability/versions/<$document_id>"
   			 }
		}
	}
}
```

**Reponse Status**

| Status Code | Description |
| ----------- | ----------- |
|200|OK|
|422|Not processable. Language Not supported|
|413|Payload too large|

**Constraints/Comments**

* 5000 characters limit for Guest Users
* 15000 character limit for signed-in users and API requests
* category --> Has to be expanded, plus is a mandatory parameter