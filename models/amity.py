from rooms import Room

class Amity():
	def __init__(self):
		self.room = []

	def create_room(self, args):
		''' Creates new room(s) '''

		print "You have successfully added the following rooom(s):"

		for r in args["<room_name>"]:
			my_room = Room()
			room_type = "Living Space" if args["Living"] else "Office" # set room type
			name = r
			self.room.append(my_room)
			print "Name: " + ''.join(name) + " | Type: " + room_type
	            
