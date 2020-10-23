import os
 
import win32file
import win32con
 
def mon_dir():
    ACTIONS = {
    1: "Created",
    2: "Deleted",
    3: "Updated",
    4: "Renamed from something",
    5: "Renamed to something"
    }
    
    FILE_LIST_DIRECTORY = 0x0001
    
    path_to_watch = 'C:/Users/jimuti/Desktop/aaa'
    print('Watching changes in',path_to_watch)
    print("开始监控文件夹",path_to_watch)
    hDir = win32file.CreateFile(
        path_to_watch,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
    )
    while 1:
        results = win32file.ReadDirectoryChangesW(
                hDir,
                1024,
                True,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                win32con.FILE_NOTIFY_CHANGE_SIZE |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SECURITY,
                None,
                None
            )
        for action, filename in results:
            full_filename = os.path.join(path_to_watch, filename)
            print("full_filename:%s,2:%s"%(full_filename,ACTIONS.get(action, "Unknown")))
           # if ACTIONS.get(action, "Unknown")
str1='dasdsa.exe'
print(str1[-4:])
