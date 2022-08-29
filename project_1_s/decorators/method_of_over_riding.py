class Editor:
    def fun(self):
        return["create a new file","execute"]
class Pycharm(Editor):
    def fun(self):
        specs=super().fun()
        specs.append("debug")
        return specs
class Vscode(Editor):
    def fun(self):
        specs=super().fun()
        specs.append("vcs")
        return specs
pyc=Pycharm()
print(pyc.fun())
vsc=Vscode()
print(vsc.fun())