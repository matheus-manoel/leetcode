class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        sorted_box_types = sorted(boxTypes, key=lambda x: x[1])
        n_items = 0

        i = len(sorted_box_types) - 1
        while truckSize and i >= 0:
            boxType = sorted_box_types[i]
            n_boxes, units_per_box = boxType[0], boxType[1]
            if truckSize - n_boxes >= 0:
                truckSize -= n_boxes
                n_items += n_boxes * units_per_box
            else:
                truckSize = 0
                n_items += truckSize * units_per_box
            i -= 1

        return n_items
