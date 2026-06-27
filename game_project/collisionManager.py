class CollisionManager:
    def __init__(self):
        pass

    def check_player_obstacle(self, player, obstacle):
        return (
            player.x < obstacle.x + obstacle.width and
            player.x + player.width > obstacle.x and
            player.y < obstacle.y + obstacle.height and
            player.y + player.height > obstacle.y
        )

    def check_player_reward(self, player, reward):
        return (
            player.x < reward.x + reward.width and
            player.x + player.width > reward.x and
            player.y < reward.y + reward.height and
            player.y + player.height > reward.y
        )