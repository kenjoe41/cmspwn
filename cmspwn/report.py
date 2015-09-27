import sys, platform, os

class Report:
    def __init__(self):
        self.fn = self.get_log_file()
        self.log = ' '.join(sys.argv)
        self.col()
	 
        
    def get_log_file(self):
	fn = os.path.dirname(os.path.abspath(__file__))+'_logs'
	fn_dirs = os.path.join(fn.split('/')[:-1])
	if not fn_dirs:
		os.mkdir(fn_dirs)
	return fn
    def col(self):
        if sys.stdout.isatty() and platform.system() != "Windows":
            self.green = '\033[32m'
            self.blue = '\033[94m'
            self.red = '\033[31m'
            self.brown = '\033[33m'
            self.grey = '\033[90m'
            self.orange = '\033[38;5;208m'
            self.yellow = '\033[93m'
            self.end = '\033[0m'
            
        else:# Disabling col for windows and pipes
            self.green = ""
            self.orange = ""
            self.blue = ""
            self.red = ""
            self.brown = ""
            self.grey = ""
            self.yellow = ""
            self.end = ""
            
    def info(self, msg):
        self.WriteTextFile("[I] " +msg)
        msg = self.green + "[I] " + msg; print(msg)

    def low(self, msg):
        self.WriteTextFile("[L] " +msg)
        msg = self.yellow + "[L] " + msg; print(msg)

    def medium(self, msg):
        self.WriteTextFile("[M] " +msg)
        msg = self.orange + "[M] " + msg; print(msg)
        
    def high(self, msg):
        self.WriteTextFile("[H] " +msg)
        msg = self.red + "[H] " + msg; print(msg)

    def status(self, msg):
        self.WriteTextFile("[-] " +msg)
        msg = self.blue + "[-] " + self.end + msg; print(msg)
        
    def message(self, msg):
        msg = "[-] " + msg; print(msg)
        self.WriteTextFile(msg)
        
    def error(self, msg):
        self.WriteTextFile("[ERROR] " +msg)
        msg = self.red + "[ERROR] " + msg; print(msg)

    def verbose(self, msg):
        if verbose:
            self.WriteTextFile("[v] " +msg)
            msg = self.grey + "[v] " + msg; print(msg)
        
    def WriteTextFile(self, msg):
        if msg:
            self.log += "\n"+msg
            with open(self.fn,"w") as f:
                f.write(self.log)
    
    def WriteHTMLFile(self):
        pass


