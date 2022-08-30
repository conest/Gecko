from .signal import SignalGroup


class Object:
    name: str
    '''Object.name: work as an unique ID'''
    signals: SignalGroup

    def __init__(self):
        self.name = "Default_Object_Name"
        self.signals = SignalGroup()

    def __str__(self) -> str:
        return f'[Object] {self.name}'

    def update(self, _delta: int):
        pass


class ObjectList:

    objects: list[Object]
    name: str

    def __init__(self, groupName: str = "ObjectGroup"):
        self.objects = []
        self.name = groupName

    def add(self, ob: Object, checkDup: bool = True):
        if checkDup:
            self._check_name_unique(ob.name)
        self.objects.append(ob)

    def delete(self, name: str) -> bool:
        '''Return False if nothing find in the list with the given name'''
        for i, o in enumerate(self.objects):
            if o.name == name:
                del self.objects[i]
                return True
        return False

    def _check_name_unique(self, name: str):
        for s in self.objects:
            if s.name == name:
                print(f'[WARNING] Find object name duplicated: {s.name} in {self.name}')

    def check_all_name(self, logout: bool = False) -> dict:
        nameDict = {}
        for s in self.objects:
            if s.name in nameDict:
                if logout:
                    print(f'[WARNING] Find object name duplicated: {s.name} in {self.name}')
                return {'dup_name': s.name}
            else:
                nameDict[s.name] = True
        return {}
