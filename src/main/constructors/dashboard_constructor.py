from src.views.dashboard_view import DashboardView
from src.controllers.dashboard_controller import DashboardController


def dashboard_constructor(page):
    view_dashboard = DashboardView(page)
    DashboardController(page,view_dashboard)
    return view_dashboard