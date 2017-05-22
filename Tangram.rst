
.. code:: python

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

.. code:: python

    [ shapes[name] for name in piece_names ]




.. parsed-literal::

    [[(4, 2), (3, 1), (2, 2), (3, 3)],
     [(2, 0), (4, 0), (4, 2)],
     [(0, 0), (1, 1), (3, 1), (2, 0)],
     [(4, 4), (4, 2), (2, 2)],
     [(4, 4), (4, 2), (2, 2)],
     [(0, 0), (0, 4), (2, 2)],
     [(0, 0), (0, 4), (2, 2)]]



.. code:: python

    def rotate(shape, angle):
        ...
        
    def translate(shape, x, y):
        """
        > translate([(0, 0), (2, 2), (4, 0)], 1, 7)
        [(1, 7), (3, 9), (5, 7)]
        """
        ...


::


      File "<ipython-input-7-204bacd0d2e4>", line 2
        ...
        ^
    SyntaxError: invalid syntax



.. code:: python

    # Encode a simple problem
    

