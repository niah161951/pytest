import time
from ctypes import windll

lib_path = r"D:\PycharmProject\untitled\SHDY\Public\DD94687.64.dll"  # 你存入该文件的路径
dd_dll = windll.LoadLibrary(lib_path)


class InputPasswordUtil:
    """
        模拟键盘输入密码内容
    """

    def input_password(self, password):
        vk = {
            '5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208,
            'w': 302, 'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504,
            'r': 304, 'i': 308, 'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206,
            '2': 202, 'b': 505, 'k': 408, '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209,
            'p': 310, 'o': 309, 't': 305, '-': 211, '=': 212, 's': 402, ';': 410
        }

        # 需要组合shift的按键。
        vk2 = {
            '"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7',
            '{': '[', '_': '-', '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1',
            '(': '9'
        }

        def down_up(code):
            dd_dll.DD_key(vk[code], 1)
            dd_dll.DD_key(vk[code], 2)

        def dd(key):
            if key.isupper():
                # 按下 500是shift键码
                dd_dll.DD_key(500, 1)
                down_up(key.lower())
                dd_dll.DD_key(500, 2)
            elif key in r'~!@#$%^&*()_+{}|:"<>?':
                dd_dll.DD_key(500, 1)
                down_up(vk2[key])
                dd_dll.DD_key(500, 2)
            else:
                down_up(key)

        # 依次输入密码字符
        for key in password:
            dd(key)
            time.sleep(0.5)