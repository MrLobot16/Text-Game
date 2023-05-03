#This is for Usable inventory Items


class item():
	def __init__(self, name):
		self.sprite = ''
		self.name = name
		self.smallSprite = ''
		self.flavorText = ''
class weapon(item):
	def __init__(self, name):
		super().__init__(name)
		self.hitText = {}

itemlist = []

empty = weapon('empty')
empty.sprite = '''       
       
       '''
empty.hitText = {'w':'With all your force you punch the wall.\nOUCH that hurt!',
' ':'You practice some of your cool ninja skills.'}
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
