from mcpi.minecraft import Minecraft
# подключение к серверу
mc = Minecraft.create()

x = 100
y = 150
z = 100
# телепорт
#mc.player.setTilePos(x, y, z)
# id блока
block = 46
# ставит блок
mc.setBlock(x, y, z, block)
mc.setBlock(x, y+1, z, block)
