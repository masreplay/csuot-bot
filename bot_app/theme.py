from dataclasses import dataclass


@dataclass
class ScheduleTheme:
    background_color: str
    on_background_color: str

    primary_color: str
    on_primary_color: str

    font_name: str = "Tajawal"


# material shade 200 , reduce 0.95
DARK_THEME = ScheduleTheme(background_color="#1f1f1f", on_background_color="#ffffff",
                           primary_color="#FFF700", on_primary_color="#000000")

# material shade 200
LIGHT_THEME = ScheduleTheme(background_color="#ffffff", on_background_color="#000000",
                            primary_color="#FFF700", on_primary_color="#000000")
