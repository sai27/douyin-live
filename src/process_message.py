import time
import win32gui
import win32con
import ctypes

groupDict = {}

def GiftHandler(groupId, userName, giftName, giftId, repeatCount, repeatEnd):
    group = None
    if groupId in groupDict:
        group = groupDict[groupId]

    if repeatEnd == 1:
        if group is None:
            return
        if group["repeatCount"] < repeatCount:
            count = repeatCount - group["repeatCount"]
            SendToProcess(f"gift#{userName}#{giftName}#{count}\r\n")
        del groupDict[groupId]
        return

    if group is not None:
        if group["repeatCount"] < repeatCount:
            count = repeatCount - group["repeatCount"]
            group["repeatCount"] = repeatCount
            SendToProcess(f"gift#{userName}#{giftName}#{count}\r\n")
    else:
        groupDict[groupId] = {
            "userName" : userName,
            "giftName" : giftName,
            "giftId" : giftId,
            "repeatCount" : repeatCount
            }
        SendToProcess(f"gift#{userName}#{giftName}#{repeatCount}\r\n")

def SendToProcess(data):
    hConsoleWnd = win32gui.FindWindow("ConsoleWindowClass", "E:\\Warcraft III\\war3.exe")
    if hConsoleWnd is not 0:
        print(f"找到 cmd 窗口！{hConsoleWnd}")
        for char in data:
            win32gui.SendMessage(hConsoleWnd, win32con.WM_CHAR, ord(char), 0)
            time.sleep(0.001)
            
    else:
        print(f"找不到 cmd 窗口！")