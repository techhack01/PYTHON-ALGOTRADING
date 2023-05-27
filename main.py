from kite_trade import *

# # First Way to Login
# # You can use your Kite app in mobile
# # But You can't login anywhere in 'kite.zerodha.com' website else this session will disconnected

user_id = "VE1904"       # Login Id
password = "Raj@9824224474"      # Login password
twofa = "584848"         # Login Pin or TOTP

enctoken = get_enctoken(user_id, password, twofa)
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.positions())
