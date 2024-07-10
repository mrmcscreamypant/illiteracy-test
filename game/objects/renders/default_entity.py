from .render import Render
from build.regester import regesterObject

@regesterObject
class DefaultEntityRender(Render):
    zorder = 1
    def draw(self,screen):
        screen.fill("blue")