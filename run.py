if __name__ == "__main__":
  try:
  	__import__("ambf").main_apikey()
  except Exception as e:
  	exit(str(e))
