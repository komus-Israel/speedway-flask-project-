from flask import Flask
from .controller import admin_controller
from .services.extensions_services import migrate, admin, db, jwt, api
from config import config
from api.documentation.admin import  namespace



def create_app(config_name):

    app = Flask(__name__)
    


    #   setup configuration
    app.config.from_object(config.config[config_name])
    config.config[config_name].init_app(app)

    #   initialize dependencies
    migrate.init_app(app, db)
    admin.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = []
    
    app.config["JWT_SECRET_KEY"] = "3243r34fegvfg"

    '''
        @dev    register blueprints
        
    '''

    
    app.register_blueprint(admin_controller.adminController, url_prefix="/admin")
    api.add_namespace(namespace)

    return app