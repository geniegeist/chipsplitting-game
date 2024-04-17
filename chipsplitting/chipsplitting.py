class Node:
    def __init__(self, value):
        self.value = value
        self.top = None
        self.right = None

    def __repr__(self):
        return f"{''.join([' '] * (4 - len(str(self.value)))) + str(self.value)}"
         
    def __str__(self):
        return f"{''.join([' '] * (4 - len(str(self.value)))) + str(self.value)}"

class CoordinateSystem:
    def __init__(self, root):
        self.root = root
        self.coordinates = []
        self.init_coordinates()

    def init_coordinates(self):
        def dfs(n):
            if not n:
                return
            res = []
            cur = n
            while cur:
                res.append(cur)
                cur = cur.top
            self.coordinates.append(res)
            dfs(n.right)
        dfs(self.root)
    
    def __str__(self):
      accu = []
      def dfs(n):
          if not n:
              return
          res = []
          cur = n
          while cur:
              res.append(cur)
              cur = cur.right
          accu.append(res)
          dfs(n.top)
      dfs(self.coordinates[0][0])

      return "\n".join([" ".join([str(v) for v in row]) for row in accu[::-1]])

    def coordinatesOf(self, node):
        for i, cols in enumerate(self.coordinates):
            for j in range(len(cols)):
                if cols[j] == node:
                    return (i, j)
        return -1