import tkinter as tk
from backend import *


def setUp():
    global manager
    manager = Manager()
    item1 = Item(2, 3)
    item2 = Item(3, 678.6)
    item3 = Item(4, 55.67)
    manager.addItem(item1)
    manager.addItem(item2)
    manager.addItem(item3)



def test():
    setUp()

    win = tk.Tk()
    global labelValues
    labelValues = []
    for i, item in enumerate(manager.getItems()):
        key = tk.Label(win, text=item.key)
        key.grid(row=i, column=0)
        selectedLabelValue = tk.StringVar(value=str(item.getValue()))
        labelValues.append(selectedLabelValue)
        valueEntry = tk.Entry(win, textvariable=selectedLabelValue)
        valueEntry.grid(row=i, column=1)
        buttonText = "update item {}".format(i+1)
        updateButton = tk.Button(
            win,
            text=buttonText,
            command=lambda selectedItem=item,
                           selectedLabelValue=selectedLabelValue:
            updateHandler(selectedItem, selectedLabelValue)
        )

        updateButton.grid(row=i, column=2)

    updateAllButton = tk.Button(win, text="update all", command=updateAllHandler)
    updateAllButton.grid(row=len(manager.getItems()), column=0, columnspan=3)
    win.mainloop()


def updateHandler(selectedItem, selectedLabelValue):
    # Update the corresponding item with the new value
    selectedItem.setValue(selectedLabelValue.get())
    # Refresh the text in the text widget
    selectedLabelValue.set(str(selectedItem.getValue()))
    # Verify that the manager object is updated
    print(f"Updated item: {selectedItem}")
    print(manager)

def updateAllHandler():
    # Initialize an empty list to store the output
    values = []
    # Iterate over the list of labelValues
    for v in labelValues:
        # Get the value of the current label as a string
        value_str = v.get()
        # Convert the string to a float and append it to the output list
        value_float = float(value_str)
        values.append(value_float)

    # Update all the items in the Manager object with the latest values
    manager.updateAll(values)
    # Refresh all the text in the Entry widgets
    for i, item in enumerate(manager.getItems()):
        labelValues[i].set(str(item.getValue()))
    # Verify that the manager object is updated
    print(manager)

if __name__ == '__main__':
    test()