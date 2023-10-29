# Learning Python with CS50
# File Extensions
# https://cs50.harvard.edu/python/2022/psets/1/extensions/

def main():
  file = input("File name:  ").strip().lower()
  dot = file.find(".")
  ext = file[dot:len(file)]

  if ".gif" in ext:
    print("image/gif")
  elif ".png" in ext:
    print("image/png")
  elif ".pdf" in ext:
    print("application/pdf")
  elif ".txt" in ext:
    print("text/plain")
  elif ".zip" in ext:
    print("application/zip")
  elif ".html" in ext:
    print("text/html")
  elif ".jpg" in ext or  ".jpeg" in ext:
    print("image/jpeg")
  else :
    print("application/octet-stream")

main()
