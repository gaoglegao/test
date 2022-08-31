import win32com.client
import win32gui
import win32api
import win32con
import win32ui
from PIL import Image
import pyautogui

def setForeground(hwnd):
 """
  将窗口设置为最前面
 :param hwnd: 窗口句柄 一个整数
 """
 if hwnd != win32gui.GetForegroundWindow():
  shell = win32com.client.Dispatch("WScript.Shell")
  shell.SendKeys('%')
  win32gui.SetForegroundWindow(hwnd)


def winShot(hwnd):
 """
  根据窗口句柄截取窗口视图
 :param hwnd: 窗口句柄 一个整数
 """
 bmpFileName = 'screenshot.bmp'
 jpgFileName = 'screenshot.jpg'

 r = win32gui.GetWindowRect(hwnd)
 hwin = win32gui.GetDesktopWindow()
 # 图片最左边距离主屏左上角的水平距离
 left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
 # 图片最上边距离主屏左上角的垂直距离
 top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
 hwindc = win32gui.GetWindowDC(hwin)
 srcdc = win32ui.CreateDCFromHandle(hwindc)
 memdc = srcdc.CreateCompatibleDC()
 bmp = win32ui.CreateBitmap()
 bmp.CreateCompatibleBitmap(srcdc, r[2] - r[0], r[3] - r[1])
 memdc.SelectObject(bmp)
 memdc.BitBlt((-r[0], top - r[1]), (r[2], r[3] - top), srcdc, (left, top), win32con.SRCCOPY)
 bmp.SaveBitmapFile(memdc, bmpFileName)

 im = Image.open(bmpFileName)
 im = im.convert('RGB')
 im.save(jpgFileName)

if __name__ == '__main__':
 setForeground(5179154)
 winShot(5179154)
 pyautogui.typewrite(message="1234",interval=0.25) #找到对应的应用  按键输入1234 间隔0.25