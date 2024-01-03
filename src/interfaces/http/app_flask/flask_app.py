from bootstrap import ApplicationBootstrap
from flask import Flask
from interfaces.http.app_flask.handlers.health_handler import HealthHandler
from waitress.server import create_server


class MainApplication():
    def __init__(self):
        _app = Flask(__name__)
        _app.add_url_rule(
            "/health",view_func=HealthHandler.as_view(name='health-status')
        )
        # 127.0.0.1/
        # 127.0.0.1/health
        # 127.0.0.1/app
        # 127.0.0.1/app/login
        # 127.0.0.1/app/reset
        # 127.0.0.1/app/dashboard
        # 127.0.0.1/api/v1/login
        # 127.0.0.1/api/v1/reset
        # 127.0.0.1/api/v1/dashboard
        self._app = _app
    
    @property
    def app(self)->Flask:
        return self._app

    async def run_server(
            self,
            app_bootstrap:ApplicationBootstrap,
            port: int
    ) -> None:
        # WORKED
        # WHILE STOPPING FOLLOW Waitress Close
        app_bootstrap.server = create_server(self.app,host="127.0.0.1",port=port)
        app_bootstrap.server.run()