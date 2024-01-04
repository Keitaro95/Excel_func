import database

"""
必要に応じて関数のコメントアウトを消してください
"""

# database.add_one('Laura', 'Smith', 'laura@smith.com')
# database.show_all()

# rowidは文字列で渡す必要があります
# database.delete_one('5')
# database.show_all()

# stuff = [
#     ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
#     ('Joshua', 'Raintree', 'josh@raintree.com')
#     ]
# database.add_many(stuff)
# database.show_all()

database.email_lookup("john@codemy.com")

