# coding: utf-8

import random

import GraphCap as gc
import GraphCapCon as gcc


class DesktopWindow:
    def __init__(self):
        print("正在枚举窗口……")
        windowList = gc.Window.EnumWindows()
        for i in range(len(windowList)):
            window = windowList[i]
            print("{0}.[{1}]{2}".format(i + 1, window.getPid(), window.getName()))
        j = int(input("请输入窗口编号："))
        self.window = windowList[j - 1]

        self.capturer = gc.DesktopCapturer()
        self.image = gc.Image()
        self.rect = gc.Rect()

        self.input = gc.DesktopInput()

    def capture(self):
        self.rect = self.window.getRect()
        # print("窗口位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        if not self.capturer.capture(self.image, self.rect):
            print("捕获图像失败：桌面超时未更新，或者窗口位置错误。")
            return None
        if self.image.getType() != gcc.IT_8UC4:
            raise Exception("图像格式错误：请将桌面设置为32位色。")
        # print("捕获位置：x={0}, y={1}, width={2}, height={3}".format(
        #    self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        dsize = gc.Size(974, 634)
        if self.rect.width != dsize.width or self.rect.height != dsize.height:
            return self.image.resize(dsize)
        else:
            return self.image

    def click(self, location, size):
        x = self.rect.x + location.x + random.randint(0, size.width - 1)
        y = self.rect.y + location.y + random.randint(0, size.height - 1)
        self.input.setMousePos(gc.Point(x, y))
        self.input.mouseLeftDown()
        self.input.mouseLeftUp()
