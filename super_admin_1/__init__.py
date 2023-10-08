from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from super_admin_1.config import App_Config


db = SQLAlchemy()


def create_app():
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-

    app = Flask(__name__)
    app.config.from_object(App_Config)
    if app.config["SQLALCHEMY_DATABASE_URI"]:
        print(f"using db")

    # Initialize CORS
    CORS(app, supports_credentials=True)

    # Initialize SQLAlchemy
    db.init_app(app)

    # imports blueprints
    from super_admin_1.shop.del_shop import del_shop
    from super_admin_1.products.restore_product import restore_product
    from super_admin_1.products.restore_product import create_product # for testing purpose by Samuel Ogboye
    from super_admin_1.products.restore_product import delete_product # for testing purpose by Samuel Ogboye
    # Import shop blueprint
    from super_admin_1.shop.routes import shop as shop_blueprint
    from super_admin_1.shop.del_shop import del_shop
    from super_admin_1.products.delete_product import product_delete
    from super_admin_1.shop.shop_activity import events
    from .shop.ban_vendor import shop

    # register blueprints
    app.register_blueprint(del_shop)
    app.register_blueprint(restore_product)
    app.register_blueprint(create_product) # for testing purpose by Samuel Ogboye
    app.register_blueprint(delete_product) # for testing purpose by Samuel Ogboye
    app.register_blueprint(product_delete)
    app.register_blueprint(events)
    app.register_blueprint(shop, url_prefix='/api/shop')
    app.register_blueprint(shop_blueprint)
    app.register_blueprint(del_shop)
    
    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from flask import Flask
# from super_admin_1.config import App_Config
# from flasgger import Swagger
# import yaml

# db = SQLAlchemy()

# # Create an instance of Swagger
# swagger = Swagger()


# def create_app():
    
#     """
#     Create a new instance of the app with the given configuration.

#     :param config_class: configuration class
#     :return: app
#     """
#     # Initialize Flask-

#     app = Flask(__name__)
#     app.config.from_object(App_Config)
#     if app.config["SQLALCHEMY_DATABASE_URI"]:
#         print(f"using db")

#     # Initialize CORS
#     CORS(app, supports_credentials=True)
#     # Load Swagger content from the file
#     with open('swagger_config.yaml', 'r') as file:
#         swagger_config = yaml.load(file, Loader=yaml.FullLoader)

#     # Initialize Flasgger with the loaded Swagger configuration
#     Swagger(app, template=swagger_config)

#     # Initialize SQLAlchemy
#     db.init_app(app)

#     # create db tables from models if not exists
#     with app.app_context():
#         db.create_all()

#     return app
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_cors import CORS
# # from flask import Flask
# # from super_admin_1.config import App_Config
# # from flasgger import Swagger
# # import yaml

# # db = SQLAlchemy()

# # # Create an instance of Swagger
# # swagger = Swagger()


# # def create_app():
    
# #     """
# #     Create a new instance of the app with the given configuration.

# #     :param config_class: configuration class
# #     :return: app
# #     """
# #     # Initialize Flask-

# #     app = Flask(__name__)
# #     app.config.from_object(App_Config)
# #     if app.config["SQLALCHEMY_DATABASE_URI"]:
# #         print(f"using db")

# #     # Initialize CORS
# #     CORS(app, supports_credentials=True)
# #     # Load Swagger content from the file
# #     with open('swagger_config.yaml', 'r') as file:
# #         swagger_config = yaml.load(file, Loader=yaml.FullLoader)

# #     # Initialize Flasgger with the loaded Swagger configuration
# #     Swagger(app, template=swagger_config)

# #     # Initialize SQLAlchemy
# #     db.init_app(app)




# #     # # Import shop blueprint
# #     # from super_admin_1.shop.routes import shop as shop_blueprint
# #     # from super_admin_1.shop.del_shop import del_shop

# #     # # imports blueprints
# #     # from super_admin_1.shop.del_shop import del_shop

# #     # # register blueprints
# #     # app.register_blueprint(del_shop)
# #     # # imports blueprints

# #     # # Testing db purpose
# #     # # from super_admin_1.models.shop_log import ShopLog
# #     # from super_admin_1.shop.shop_activity import events

# #     # # register blueprints
# #     # app.register_blueprint(events)

# #     # # # Register blueprints
# #     # from .shop.ban_vendor import shop

# #     # app.register_blueprint(shop, url_prefix='/api/shop')


# #     # # Register the shop Blueprint
# #     # app.register_blueprint(shop_blueprint)
# #     # app.register_blueprint(del_shop)
    
# #     # create db tables from models if not exists
# #     with app.app_context():
# #         db.create_all()

# #     return app