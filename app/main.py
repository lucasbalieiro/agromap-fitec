from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.roles import router as roles_router


def create_application():
    application = FastAPI(
        title="AgroMap API"
    )
    application.include_router(roles_router)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    @application.get("/ping")
    def root():
        return {"message": "Pong"}

    return application


app = create_application()
