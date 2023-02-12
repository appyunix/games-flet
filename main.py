
from flet import *
import time
from view import *

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = MainAxisAlignment.START
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.theme_mode = ThemeMode.LIGHT
#     page.theme = Theme(font_family="Poppin-medium")
#     page.fonts={
#         "Poppin-medium" : "/font/Poppins-Medium.ttf"
#     }

    def route_change(route):
        print(page.route)
        page.views.clear
        page.views.append(
            rouute(page)[page.route]

        )


    page.on_route_change = route_change
    page.go('/dice')



    # // route temp 
    
app(target=main, view=WEB_BROWSER, web_renderer="html")
