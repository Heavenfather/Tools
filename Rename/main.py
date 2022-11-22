import os

osPath = os.getcwd()
def main():
    while True:
        try:
            startIndex=int(input("请输入一个数字开始的索引:"))
            break
        except:
            pass
    
    while True:
        try:
            changeCount=int(input("需要修改的个数(负数则全部更改):"))
            break
        except:
            pass

    files=get_all_files()
    currentIndex = startIndex
    notChangedFiles = []
    fileTotal = len(files)
    if changeCount < 0:
        changeCount = fileTotal - startIndex

    if changeCount <= 0:
        return

    for file in files:
        if currentIndex >= startIndex + changeCount:
            break        
        result,currentIndex=rename_file(file,startIndex,currentIndex)
        if result == False:
            notChangedFiles.append(file)
    startIndex = currentIndex
    for file in notChangedFiles:
        if os.path.exists(file):
            continue
        result,currentIndex = rename_file(file,startIndex,currentIndex)

def  is_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def get_all_files():
    files=os.listdir(osPath)
    try:
        files.remove('heaven_rename.exe')
    except ValueError:
        pass
    return files

def rename_file(file,startIndex,renameIndex):
    fileName,fileExtension = get_file_info(file)
    srcPath = osPath + "/" + file
    desPath = osPath + "/" + str(renameIndex) + fileExtension
    if is_number(fileName):
        if int(fileName) <= startIndex:
            return True,renameIndex
    renameIndex += 1
    if os.path.exists(desPath):   
        return False,renameIndex
    os.rename(srcPath,desPath)
    return True,renameIndex
    
def get_file_info(file):
    info = str.split(file,'.')
    file_name = info[0]
    file_extension = ''
    if len(info) > 1:
        file_extension = '.' + info[len(info) - 1]
    return file_name,file_extension

main()
input('执行结束,按回车关闭!')