import random
import copy

class Hat:
    def __init__(self,**kwargs):
        self.kwargs = kwargs
        self.contents = []

        for key,value in self.kwargs.items():
            self.contents.extend([key]*value)
    def draw(self,rep):
        self.drawn_balls = []
        self.balls = len(self.contents)
        if(self.balls>rep):
            for i in range(rep):
                drawn_ball = random.choice(self.contents)
                self.drawn_balls.append(drawn_ball)
                self.contents.remove(drawn_ball)
        else:
            self.drawn_balls = self.contents
        return self.drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0

    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
    
        success = True
        for ball, count in expected_balls.items():
            if drawn_balls.count(ball) < count:
                success = False
                break
        
        if success:
            m += 1

    return m / num_experiments



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=50)
