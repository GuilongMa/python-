from queue import Queue


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    if not root:
        return
    print(root.val, "->", end='')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    pre_order(root.left)
    print(root.val, "->", end='')
    pre_order(root.right)


def post_order(root):
    if not root:
        return
    pre_order(root.left)
    pre_order(root.right)
    print(root.val, "->", end='')


def level_traver(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.val, "->", end='')
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)


if __name__ == "__main__":
    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless, album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    pre_order(singer)
    print("\n")
    in_order(singer)
    print("\n")
    post_order(singer)
    print("\n")
    level_traver(singer)
