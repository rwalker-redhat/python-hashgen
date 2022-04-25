import fastapi
import uvicorn

from api import health, hashgen

main_app = fastapi.FastAPI()


def configure():
    configure_routing()


def configure_routing():
    main_app.include_router(health.router)
    main_app.include_router(hashgen.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(main_app, host='0.0.0.0', port=8000)
else:
    configure()
