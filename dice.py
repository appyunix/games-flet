from flet import *

max_width = 400
current_period = "8164007"
timer_minute = "00"
timer_second = "30"
sliderval = 30
slideramt = sliderval * 0.9
default_color = "#AAA8A8"
default_bgcolor = "#F0F2FF"
current_page = ""
less_than = Text(value="30",size = 26)
great = Text(value="20",size = 26)
current_period_text = Text(value=current_period, size=30)
minutes = Text(value=timer_minute,size=26)
seconds = Text(value=timer_second,size=26)

class AppTitle(UserControl):
    def __init__(self):
        super().__init__()


    def header(self):
        return Container(
                    width= max_width,
                    content=Column([Row(
                        controls=[
                            IconButton(
                                icon=icons.ARROW_BACK_IOS_ROUNDED
                            ),
                            Text(
                                value="Dice",
                                size=28,
                            ),
                            Text(
                                value="Rules",
                            )
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    ),
                    Divider()
                    
                    ]
                    )
                )

    def period(self):
        return Container(
            width=max_width,
            content=Row(

                controls=[
                    Column([
                        Text(value="Period",
                        size=24,
                        color=default_color
                        ),
                        current_period_text
                    ]
                    ),
                    Column(
                        horizontal_alignment=CrossAxisAlignment.END,
                        controls=[
                        Text(value="Count Down", size=26,
                        color=default_color),
                        Row(
                            [
                                Container(
                                    border_radius=border_radius.only(9,0,9,0),
                                    bgcolor= "#F0F2FF",
                                    width = 47,
                                    height = 47,
                                    content= minutes,
                                    alignment=alignment.center
                                ),
                                Container(
                                    border_radius=border_radius.only(0,9,0,9),
                                    bgcolor= "#F0F2FF",
                                    width = 47,
                                    height = 47,
                                    content= seconds,
                                    alignment=alignment.center
                                )
                            ]
                        )]
                    )
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )

    def multiplier(self):
        return Container(
            width = max_width,
            content = Row(
                controls=[
                    Container(
                        width = 175,
                        height = 90,
                        bgcolor= default_bgcolor,
                        border_radius=border_radius.only(10,0,10,0),
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    value="Less Than",
                                    size = 20,
                                    color=default_color,
                                ),less_than
                            ]
                            
                        )
                    ),
                # ui design for less than amt
                    Container(
                        width = 175,
                        height = 90,
                        bgcolor= default_bgcolor,
                        border_radius=border_radius.only(0,10,0,10),
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Text(
                                    value="Less Than",
                                    size = 20,
                                    color=default_color,
                                ),great
                            ]
                        )
                    )
                ]
            )
        ) 

    def sliderchange(self, e):
        less_than.value = round(e.control.value)
        sliderval =round(e.control.value)
        slideramt = round(96 / int(sliderval), 2)
        great.value = slideramt
        self.update()

    def slider(self):
        return Slider(min=1.0, max=90.0, value = 30, divisions=89, label="{value}", on_change=self.sliderchange, width= 400)

    def button(self):
        return Container(
            width = max_width,
            bgcolor="#43E570",
            height= 70,
            alignment=alignment.center,
            border_radius= border_radius.all(10),
            content=Text(value = "Bet now", size = 20)

        )

    def record(self):
        return Container(
            Text(
                value = "Dice Records",size=22
            )
        )
    def functionlist(self):
        return Container(
            width=46,
            content=Column(
                controls=[
                    Container(
                        width=45,
                        height=45,
                        bgcolor="#43E570",
                        border_radius=border_radius.all(8),
                        alignment=alignment.center,
                        content=Text(
                            value='46',
                            size=20,
                            color='white'

                        )
                                            ),
                                            Text(value='100',size=20)
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.SPACE_AROUND
                
            )
        )
    def build(self):
        return Container(
            width = max_width,
            height = 720,
            content=Column([
                self.header(),
                self.period(),
                Container(
                    height=2
                ),
                self.multiplier(),
                self.slider(),
                self.button(),
                Divider(),
                self.record(),
                self.functionlist(

                )
                ]
            )
        )
