#This is for Usable inventory Items


class item():
	def __init__(self, name):
		self.sprite = ''
		self.name = name
		self.smallSprite = ''
		self.flavorText = ''
		self.type = 'item'
class weapon(item):
	def __init__(self, name):
		super().__init__(name)
		self.hitText = {}
		self.type = 'weapon'

itemlist = []

empty = weapon('empty')
empty.sprite = '''       
       
       '''
empty.hitText = {'w':'With all your force you punch the wall.\nOUCH that hurt!',
' ':'You practice some of your cool ninja skills.',
'e':'You jab the monster right in the face!'}
itemlist += [empty]

stick = weapon('stick')
stick.sprite = ''' \| /  
  |/   
  |    '''
stick.hitText = {'w':'You try to break through the wall with the stick.\nIt didn\'t work.',
' ':'You swing the stick around like a staff.',
'e':'You poke the monster right in the eyes!\nOUCH!'}
stick.smallSprite = '''



'''
itemlist += [stick]

key = item('key')
key.sprite = '''  _    
 │o│┐┐ 
  ¯    '''
itemlist += [key]
