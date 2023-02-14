class stack:
    def __init__(self):
        self.data= []
        self.last_index=-1
    def add(self,data):
        self.data.append(data)
        self.last_index += 1
    def pop(self):
        result = None
        if self.last_index==-1:
            print('stack is empty')
        else:
            result = self.data.pop(self.last_index)
            self.last_index -= 1
        return result

    def print(self):
        print('Stack Elements are:')
        for i in range(self.last_index+1):
            print(self.data[i])
        print('----------------------------')

def main():
        s0 = stack()
        s0.add(1)
        s0.add(2)
        s0.add(3)
        s0.print()
        s0.pop()
        s0.print()

if __name__ == "__main__":
        main()