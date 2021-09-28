class FileSystem:

    def __init__(self):
        self.root = collections.defaultdict(dict)
        

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(list(self.root[''].keys()))
        path = path.split("/")
        root = self.root
        
        for p in path:
            root = root[p]
            
        if "#" in root:
            return [path[-1]]
        else:
            
            return sorted(list( k for k in root.keys()))
        

    def mkdir(self, path: str) -> None:
        path = path.split("/")
        root = self.root
        print(path)
        for p in path:
            if p not in root:
                root[p] = {}
            root = root[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")
        root = self.root
        
        for p in path:
            if p not in root:
                root[p] = {}
            root = root[p]
        
        if "#" in root:
            getVal = root.get("#")
            root["#"] = getVal + content
            return  root["#"]
        else:
            root["#"] = content
            return content
        
        

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")
        root = self.root
        
        for p in path:
            root = root[p]
            
        return root["#"]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)