REST API
- REST: "Representational State Transfer"
- API: "Application Programming Interface"
- is set-up with a bunch of endpoints wherein users can connect in order to send request to a particular endpoint which returns a specific response
- e.g. A request for the info of 'number of views' for a specific video, would specifically return that request.  But if the request is not possible like if the video doesn't exists, then a particular response would be returned

FLASK RESTFUL API (workflow)
(1) Pip install 'flask-restful'
(2) 'from flask_restful import Api, Resource'
(3) Create Resource (define Class, inherit 'Resource')
    - ensure that API's return value is JSON serializable
(4) Override methods (define Function under Class)
(4) Register Resource
    - define URL parameters