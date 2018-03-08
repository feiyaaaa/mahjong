from zigong_majiang.ai.ves_ai import VesAI
from zigong_majiang.rule.tile import Hands
from zigong_majiang.rule.tile_convert import TilesConverter

tiles_18 = TilesConverter.string_to_18_array(tongzi="1245679", tiaozi="134479")
print(Hands(tiles_18))
ves = VesAI(2)
ves.calc_effective_cards(tiles_18, 2)
