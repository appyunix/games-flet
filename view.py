from flet import *
# from dice import *
from dice import *
from minesweeper import minesw

def rouute(page):
    
        return {
            '/':View(
                route='/',
                controls=[
                    AppTitle()
                ]
            ),
            '/mine':View(
                route='/mine',
                controls=[
                    minesw()
                ]
            ),
            '/dice':View(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                route = '/dice',
                controls=[
                    AppTitle()
                ]
            )
        }