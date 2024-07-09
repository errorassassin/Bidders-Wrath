class Player1:
  def __init__(self):
    self.name = 'Player 1'
    self.score = 0

  def add_score(self, score):
    self.score += score

  def bid(self, purse, current_bids):
    return int(input(f'{self.name} bids: '))
  
  def round_result(self, my_index,  bids, results):
    self.add_score(results[my_index-1])

class Player2:
  def __init__(self):
    self.name = 'Player 2'
    self.score = 0

  def add_score(self, score):
    self.score += score

  def bid(self, purse, current_bids):
    return int(input(f'{self.name} bids: '))
  
  def round_result(self, my_index,  bids, results):
    self.add_score(results[my_index-1])

class Player3:
  def __init__(self):
    self.name = 'Player 3'
    self.score = 0

  def add_score(self, score):
    self.score += score

  def bid(self, purse, current_bids):
    return int(input(f'{self.name} bids: '))
  
  def round_result(self, my_index,  bids, results):
    self.add_score(results[my_index-1])

class Player4:
  def __init__(self):
    self.name = 'Player 4'
    self.score = 0

  def add_score(self, score):
    self.score += score

  def bid(self, purse, current_bids):
    return int(input(f'{self.name} bids: '))
  
  def round_result(self, my_index,  bids, results):
    self.add_score(results[my_index-1])