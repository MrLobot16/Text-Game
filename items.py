class item():
	def __init__(self, name):
		self.sprite = ''
		self.name = name
		self.smallSprite = ''
		self.flavorText = ''
class weapon(item):
	def __init__(self, name):
		super().__init__(name)

itemlist = []

empty = item('empty')
empty.sprite = '''       
       
       '''
itemlist += [empty]

stick = weapon('stick')
stick.sprite = ''' \| /  
  |/   
  |    '''
stick.smallSprite = '''



'''
itemlist += [stick]

key = item('key')
key.sprite = '''  _    
 │o│┐┐ 
  ¯    '''
itemlist += [key]
