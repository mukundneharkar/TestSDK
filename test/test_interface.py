class LMResonseInterface:
  def success_callback(self, path: str, file_name: str):
    pass

  def error_callback(self, full_file_name: str):
    pass


class MyResponse(LMResonseInterface):

  def success_callback(self, path: str, file_name: str) -> str:
    print("in success_callback")

  def error_callback(self, full_file_name: str) -> dict:
    print("in error_callback")


class MyResponse1(object):

  def success_callback(self, path: str, file_name: str) -> str:
    print("in success_callback")

  def error_callback(self, full_file_name: str) -> dict:
    print("in error_callback")


myobj = MyResponse1()
print(isinstance(myobj, LMResonseInterface))
myobj.success_callback("path", "ad")
myobj.error_callback("path")
