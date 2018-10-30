from unittest.mock import MagicMock


result = MagicMock()
result.a = 3
result.b = "Hi"
result.get_my_ip = MagicMock(return_value=['1', 2])


a = result.get_my_ip()

print( result.get_my_ip )



# result.json = MagicMock(return_value={'ip': '1.1.1.1'})
