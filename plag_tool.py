from middleware import *
while(True):
      print "Welcome to command line console of Plag tool\n"
      print "1.List files \n"
      print "2.Plag check on files\n"
      print "3.Pattern\n"
      print "4.Quit : Quit from application\n"
      option = raw_input("Enter your choice from [1-4]\n")
      if option == "1":
          files = os.listdir(UPLOAD_FOLDER)
          for file in files:
              print file
              

