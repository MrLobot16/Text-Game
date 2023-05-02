class item():
	def __init__(self, name):
		self.sprite = None
		self.name = name
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
itemlist += [stick]

key = item('key')
key.sprite = '''  _    
 │o│┐┐ 
  ¯    '''
itemlist += [key]
