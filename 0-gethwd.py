import win32gui

hwnd_title = dict()


def _get_all_hwnd(hwnd, mouse):
 if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
  hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(_get_all_hwnd, 0)
for wnd in hwnd_title.items():
 print(wnd)


#直接通过名字找id  自己看场合用 
handle = win32gui.FindWindow(None, '微信')
print("微信的窗口:",handle)