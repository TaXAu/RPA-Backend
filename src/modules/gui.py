from src.modules.base import BaseModule
import pyautogui as pag


def getScreennSize():
    return pag.size()


class MouseMove(BaseModule):
    id = "mouse_move"
    name = "Mouse Move Module"
    version = "0.0.1"
    description = "鼠标移动到指定位置"

    def run(self, x: str, y: str):
        pag.moveTo(int(x), int(y))


class MouseMoveTo(BaseModule):
    id = "mouse_move_to"
    name = "Mouse Move To Module"
    version = "0.0.1"
    description = "鼠标移动到指定位置"

    def run(self, x: str, y: str):
        pag.moveTo(int(x), int(y))


class MouseClick(BaseModule):
    id = "mouse_click"
    name = "Mouse Click Module"
    version = "0.0.1"
    description = "鼠标点击"

    def run(self, x: str, y: str):
        pag.click(int(x), int(y))


class MouseDoubleClick(BaseModule):
    id = "mouse_double_click"
    name = "Mouse Double Click Module"
    version = "0.0.1"
    description = "鼠标双击"

    def run(self, x: str, y: str):
        pag.doubleClick(int(x), int(y))


class MouseRightClick(BaseModule):
    id = "mouse_right_click"
    name = "Mouse Right Click Module"
    version = "0.0.1"
    description = "鼠标右键点击"

    def run(self, x: str, y: str):
        pag.rightClick(int(x), int(y))


class MouseDrag(BaseModule):
    id = "mouse_drag"
    name = "Mouse Drag Module"
    version = "0.0.1"
    description = "鼠标拖拽到指定位置"

    def run(self, x1: str, y1: str, x2: str, y2: str):
        pag.dragTo(int(x2), int(y2), button="left")


class KeyPress(BaseModule):
    id = "key_press"
    name = "Key Press Module"
    version = "0.0.1"
    description = "按下指定键"

    def run(self, key: str):
        pag.press(key)
