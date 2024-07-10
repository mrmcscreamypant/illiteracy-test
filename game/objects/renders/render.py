from game.objects.object import GameObject
from build.regester import regesterObject

class FakeArray:
    """
    Workaround for py2js as it does not like .append for some reason
    """
    def push(*kw):
        pass

_renders = FakeArray()

@regesterObject
class Render(GameObject):
    def _regester(self):
        super()._init()
        print(f"Render {self.__class__} regestered")
        _renders.push(self)

    def draw(self,screen):
        pass