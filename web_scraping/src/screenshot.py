import pathlib
from htmlwebshot import WebShot


class HTMLWebShotEngine:
    def __init__(self):
        self.shot = WebShot()
        self.shot.flags = ["--quiet",
                           "--enable-javascript", "--no-stop-slow-scripts"]

    def take_screenshot(self, source: str, output_path: pathlib.Path) -> str:
        return self.shot.create_pic(url=source, output=output_path)
