class Solution:
    def findDuplicate(self, paths: 'List[str]') -> 'List[List[str]]':
        def processinput(inputstr):
            files = inputstr.split(' ')
            folder, filecontent = files[0], files[1:]
            filename, content = [], []
            for file in filecontent:
                leftpidx = file.index('(')
                filename.append(file[:leftpidx])
                content.append(file[leftpidx+1:-1])
            return folder, filename, content
        res = {}
        for inputstr in paths:
            folder, filenamelist, contentlist = processinput(inputstr)
            for filename, content in zip(filenamelist, contentlist):
                if content not in res:
                    res[content] = [folder+'/'+filename]
                else:
                    res[content].append(folder+'/'+filename)
        return [val for val in res.values() if len(val) > 1]    
