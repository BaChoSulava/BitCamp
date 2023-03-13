file_name = input("what is the file name? ")
splited_name = file_name.split(".")
file_types = {
            "gif": "Graphics Interchange Format",
            "mp4": "MPEG-4 Part 14",
            "mov": "QuickTime Movie",
            "avi": "Audio Video Interleave",
            "webm": "WebM video",
            "mkv": "Matroska video"
            }
if splited_name[-1] in file_types.keys():
    print(f"{file_name} is a \"{file_types[splited_name[-1]]}\" file")