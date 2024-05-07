class LogAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        self.file = open(self.filepath, 'r')
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line
        else:
            self.file.close()
            raise StopIteration

    def analyze_logs(self):
        for log_entry in self:
            if "Failed access" in log_entry:
                print("Alert: ", log_entry.strip())


# Usage
log_analyzer = LogAnalyzer('network_logs.txt')
log_analyzer.analyze_logs()
