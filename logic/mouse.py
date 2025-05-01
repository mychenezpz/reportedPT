from logic.kmnet import kmnet_move

class Mouse:
    def process_data(self, data):
        x, y, w, h, cls = data
        kmnet_move(x, y)

mouse = Mouse()