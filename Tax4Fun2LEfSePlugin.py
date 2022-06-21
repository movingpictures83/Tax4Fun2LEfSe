import PyPluMA

class Tax4Fun2LEfSePlugin:
    def input(self, inputfile):
        paramfile = open(inputfile, 'r')
        params = dict()
        for line in paramfile:
           contents = line.strip().split('\t')
           params[contents[0]] = contents[1]
        self.tax4funfile = open(PyPluMA.prefix()+"/"+params["tax4fun"], 'r')
        self.categories = open(PyPluMA.prefix()+"/"+params["categories"],'r')

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        # Firstline
        firstline = self.tax4funfile.readline()
        firstline = 'Sample'+firstline
        outfile.write(firstline)
        # Category line
        outfile.write("category\t")
        cats = []
        self.categories.readline()
        for line in self.categories:
            contents = line.strip().split(',')
            cats.append(contents[1])
        for i in range(0, len(cats)):
            outfile.write(cats[i])
            if (i != len(cats)-1):
                outfile.write('\t')
            else:
                outfile.write('\n')
        # Rest as is
        for line in self.tax4funfile:
            outfile.write(line)
            
