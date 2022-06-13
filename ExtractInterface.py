import sys

'''
Problem:
Multiple clients are using the same part of a
class interface.
'''
class WrongExportFile(object):
    def __init__(self, path):
        self.path = path;
    def export_to_word(self):
        return "Export to word from path {}".format(self.path);
    def export_to_pdf(self):
        return "Export to pdf from path {}".format(self.path);

'''
Solution:
Build an interface and extract the methods.
'''
class ExportFile(object):
    def __init__(self, path):
        self.path = path;
    
    def export(self):
        # code here.
        pass;

class ExportWord(ExportFile):
    def export(self):
        return "Export to word from path {}".format(self.path);

class ExportPdf(ExportFile):
    def export(self):
        return "Export to pdf from path {}".format(self.path);

try:
    file_type = sys.argv[1];
    path = sys.argv[2];
    if file_type == 'pdf':
        pdf = ExportPdf(path);
        print(pdf.export());
    elif file_type == 'word':
        word = ExportWord(path);
        print(word.export());
except Exception as e:
    print(e);