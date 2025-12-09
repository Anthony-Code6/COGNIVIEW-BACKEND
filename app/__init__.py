from fastapi import FastAPI
from app.sheduler_task import Limpiar_Imagenes
from apscheduler.schedulers.background import BackgroundScheduler
# RUTAS
from .api.routes.paciente_routes import paciente_route
from .api.routes.analisis_routes import analisis_route
from .api.routes.auth_routes import auth_route
# CONFIGURACIONES
from fastapi.middleware.cors import CORSMiddleware
from .config.bearer import custom_openapi
# from .sheduler_task import Limpiar_Imagenes

def create_app():
    app = FastAPI(title="CogniView API", version="1.0.0")

    scheduler = BackgroundScheduler()

    @app.on_event("startup")
    def start_scheduler():
        scheduler.add_job(
            Limpiar_Imagenes,
            trigger='interval',
            minutes=1,
            id='limpiar_archivos',
            replace_existing=True
        )
        scheduler.start()

    # REGISTRO DE LAS RUTAS
    app.include_router(analisis_route,prefix='/analisis',tags=["Analisis"])
    app.include_router(auth_route,prefix='/auth',tags=["Auth"])
    app.include_router(paciente_route,prefix="/paciente",tags=["Pacientes"])

    # INTEGRACION DEL BEARER - SWAGGER
    app.openapi = lambda:custom_openapi(app)

    # Orígenes permitidos
    origins = [
        "*"  # permitir todo (no recomendado en producción)
    ]

    # Agrega el middleware de CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # también puedes usar ["*"]
        allow_credentials=False,
        allow_methods=["*"],  # permite todos los métodos (GET, POST, PUT, etc.)
        allow_headers=["*"],  # permite todos los headers
    )

    return app