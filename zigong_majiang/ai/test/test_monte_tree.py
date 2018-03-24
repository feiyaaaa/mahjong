from zigong_majiang.ai.game_state import GameState
from zigong_majiang.ai.monte_tree import TreeNode, tree_search, N_SIMS
from zigong_majiang.log.logger import Logger
from zigong_majiang.simulator.client import Client
from zigong_majiang.simulator.game_server import GameServer
import logging
import cProfile


def test_monte():
    Logger.init()
    log = logging.getLogger("mahjong")
    server = GameServer()
    client1 = Client(1)
    client2 = Client(2)
    client3 = Client(3)
    server.bind(client1)
    server.bind(client2)
    server.bind(client3)
    server.init()
    server.deal()
    tile = server.tiles.pop(0)
    client1.touch_tile(tile)

    hands = [client1.hands(),
             client2.hands(),
             client3.hands()]
    discards = [[], [], []]
    melds_3 = [[], [], []]
    melds_4 = [[], [], []]
    log.info(hands)
    game_state = GameState(hands=hands, discards=discards, melds_3=melds_3, melds_4=melds_4)
    game_state.check()

    tree_node = TreeNode(net=None, game_state=game_state)

    node = tree_search(tree_node, N_SIMS, server)
    print(node.touch_tile, node.discard_tile)


cProfile.run("test_monte()")
