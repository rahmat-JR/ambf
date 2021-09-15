import os, sys
if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			os.system("rm -f .__apikey__.txt")
			exit(" [!] berhasil menghapus api key")
		else:
			print(" [?] cara menggunakan : ")
			exit(" [!] ketik : python run.py remove")
	try:
		__import__("ambf").main()
	except Exception as e:
		exit(str(e))
