from Sequence import Sequence

class SequenceParser():

    @staticmethod
    def plain(file_name):
        """

        :param file_name: data file name
        :return: Sequence object
        """
        with open(file_name) as f:
            string = ''.join([line.strip() for line in f.readlines()])
            return [Sequence(0, string)]

    @staticmethod
    def FASTQ(file_name):
        """

        :param file_name: data file name
        :return: list of Sequences
        """
        with open(file_name) as f:
            lines = f.readlines()
        result = []
        current_sequence = None
        current_line = 0
        for line in lines:
            line = line.strip()
            if len(line) == 0:continue
            if line[0] == "@":
                current_line = 0
                result.append(Sequence(line[1:], ""))
            if current_line == 1:
                result[-1].sequence = line
            current_line += 1
        return result

    @staticmethod
    def EMBL(file_name):
        with open (file_name) as f:
            lines = f.readlines()
        result = []
        state = 0 #0-looking for new sequence, 1 - looking for beginning of sequence, 2 - for end of seq
        states = ["ID","SQ","//"]
        for line in lines:
            line = line.strip()
            if len(line) == 0:continue
            if line[0:2] != states[state]:
                if state == 2:
                    result[-1].sequence += ''.join(line.split()[:-1]).upper()
                continue
            if state == 0:
                id = line.split()[1]
                result.append(Sequence(id, ""))
            state = (state+1) % 3
        return result

    @staticmethod
    def FASTA(file_name):
        with open(file_name) as f:
            lines = f.readlines()
        result = []
        for line in lines:
            line = line.strip()
            if len(line) == 0:continue
            if line[0] == ">":
                id = line.split()[0][1:]
                result.append(Sequence(id, ""))
            else:
                result[-1].sequence += line
        return result

    @staticmethod
    def GenBank(file_name):
        with open(file_name) as f:
            lines = f.readlines()
        result = []
        state = 0 #0-looking for new sequence, 1 - looking for beginning of sequence, 2 - for end of seq
        states = ["LOCUS","ORIGIN","//"]
        for line in lines:
            line = line.strip()
            if len(line) == 0:continue
            if line.split()[0] != states[state]:
                if state == 2:
                    result[-1].sequence += ''.join(line.split()[1:]).upper()
                continue
            if state == 0:
                id = line.split()[1]
                result.append(Sequence(id, ""))
            state = (state+1) % 3
        return result
