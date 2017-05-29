shapes = {
    'square': [(0,0), (1,1), (2,2), (1,-1)],
    'medium triangle': [(0,0), (2,2), (2,0)],
    'parallelogram': [(0,0), (1,1), (3,1), (2,0)],
    'small triangle': [(0,0), (1,1), (2,0)],
    'big triangle': [(0,0), (2, 2), (4,0)]
}

piece_names = [
    'square',
    'medium triangle',
    'parallelogram',
    'small triangle',
    'small triangle',
    'big triangle',
    'big triangle'
]

[ shapes[name] for name in piece_names ]

def rotate(shape, angle):
    ...
    
def translate(shape, x, y):
    """
    > translate([(0, 0), (2, 2), (4, 0)], 1, 7)
    [(1, 7), (3, 9), (5, 7)]
    """
    ...


