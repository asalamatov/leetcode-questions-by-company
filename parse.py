res: str = ""

class Line:
    def __init__(self, line) -> None:
        self.__lst = [i.strip() for i in line.split('|') if i]
        self.__title = get_title(line)
        self.__root = "https://leetcode.com/problems/"
        self.__route = self.__lst[1].replace(" ", "-").lower()

        for i in range(len(self.__lst)):
            self.__lst[1] = self.__root + self.__route + "/"
        
    def get_list(self):
        return self.__lst
    
    def get_formatted_line(self):
        return f'| {self.__lst[0]} | [{self.__title}]({self.__lst[1]}) | {self.__lst[2]} | {self.__lst[3]} |\n'


def get_title(line):
    return [i.strip() for i in line.split('|') if i][1]

def read_file(file_path):
    with open(file_path) as file:
        global res
        res = ""
        data = file.readlines()
        res += ''.join(data[:6])
        data = data[6:]
        # print(data)
        for line in data:
            title = get_title(line)
            lineObj = Line(line).get_list()
            res += f'| {lineObj[0]} | [{title}]({lineObj[1]}) | {lineObj[2]} | {lineObj[3]} |\n'
        file.close()


read_file(file_path="README.md")
# print(res)

with open("TestREADME.md", 'w') as file:
    file.write(res)

root = "https://leetcode.com/problems/"

line = "| 717 | 1-bit and 2-bit Characters |  Easy | Google |"
lineObj = Line(line)


## testing cases

# print(lineObj.get_list())
# pretty_line_list = [i.strip() for i in line.split('|') if i]
# print(pretty_line_list)
# route = pretty_line_list[1].replace(" ", "-").lower()
# print(root + route)

def add(a, b):
    return a+b