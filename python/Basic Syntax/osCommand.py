import os

current_folder = os.path.dirname(__file__)

# Get current path
current_path = os.getcwd()
print("current path is :",current_path)

# Change path
os.chdir('/Users/meihua')
current_path = os.getcwd()
print("current path is :",current_path)

# Get folders' name in 'Douments' folder of current path
foldernames = os.listdir('Documents')
print("Existing folders are:")
print(foldernames)

