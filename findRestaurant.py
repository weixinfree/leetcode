class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        commons = set(list1) & set(list2)

        if not commons:
            return []

        def index(r):
            return list1.index(r) + list2.index(r)

        l = [(index(r), r) for r in commons]
        min_index = min(l)[0]
        
        return [item[1] for item in l if item[0] == min_index]


        
        