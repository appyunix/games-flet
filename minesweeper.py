from flet import *
import time 


_bgcolor = "#EDF3FF"

def on_pan_update(e: DragUpdateEvent):
    e.control.top = max(0, e.control.top + e.delta_y)
    e.control.left = max(0, e.control.left + e.delta_x)
    e.control.update()

def onclk(e: ContainerTapEvent):
    global _bgcolor

    for i in images.controls:

        if i == e.control:
            e.control.bgcolor = colors.RED_500
            e.control.content.controls[1].visible = True
            page.update()
            time.sleep(1)
            e.control.content.controls[1].visible = False
            page.update()
            print(images.controls.index(e.control) + 1)

onclick = Text(value="+2.02")
images = GridView(
    expand=1,
    runs_count=5,
    # max_extent=100,
    child_aspect_ratio=1.0,
    spacing=5,
    run_spacing=5,
    padding=10
)
def minesw():
    return Container(
        # bgcolor= colors.RED,
        width=400,
        content=images
    )



# rand = ["#3F51B5", "#4CAF50", "#"]
for i in range(0, 25):
    images.controls.append(
        Container(
            bgcolor=_bgcolor,
            border=border.all(1, colors.BLACK12),
            border_radius=10,
            on_click=onclk,
            alignment=alignment.center,

            content=Column([
                    Text(value="+2.02", visible=False, color=colors.BLACK),
                    Image(
                        src="/dynamite.png",
                        width= 60,
                        visible = False
                    )

                            ]
            )

        )
    )

