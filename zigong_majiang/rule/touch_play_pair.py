from zigong_majiang.rule.tile import Tile


class TouchPlayPair(object):
    def __init__(self, touch_card, play_card):
        self.touch_card = Tile(touch_card)
        self.play_card = Tile(play_card)

    def __str__(self):
        return "摸牌:{},打牌:{}".format(self.touch_card.__str__(), self.play_card.__str__())
