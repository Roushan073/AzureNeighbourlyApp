from os import environ

#--------- Flask settings
SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
SERVER_PORT = int(environ.get('SERVER_PORT', '5555'))
FLASK_DEBUG = False # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
API_URL = "https://azure-neighbour-fapp.azurewebsites.net/api"

# for local host if Azure functions served locally
# API_URL = "http://localhost:7071/api"
