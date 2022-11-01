# managing tutorial
A detailed description of managing your automations

## Important Note

***When something unexpected happens when your automation executes, you can always terminate it directly by moving your mouse to the very corner of your computer screen! ***

## Converting

- After you finished editing an automation, under mainmenu frame you are able to find the convert button. When click, your automations will be converted to a python source code file
-  Beside the button, you will be able to select your converting option. There are two types (technically 3) converting options:
  1. timer: Select a timer and convert, timer activations means that the program will be started after chosen seconds passed.
  2. Hotkey activation (not reusable): Record a/multiple activation hotkeys and convert. Also the default setting is not reusable so you do not to intentionally choose it. Hotkey activation means that after executing, when you hit your recorded hotkey the automation will run.
  3. Hotkey activation (reusable): Record a/multiple activation hotkeys and convert. You will have to turn the reusable on manually. Reusable means that whenever you click your hotkey the automation will run one time but will not stop, instead it essentially works as a custom hotkey to your computer where whenever you click it the automation will run one time. (caution! Don't activate another time when your current automation hasn't finish)

## File management
Under the file management frame, you are able to see all your records and you can conveniently select a record and delete all of its associations (include .json, .py and all the associating screenshot)

## Automation manager 

### Description
Automation manager frame allows you to execute the converted python files in pyscript folder (easier management)
- Existing pyscripts shows all the avaiable converted automations stored in the pyscript folders
- Active automations shows all the active scripts
- Finished automations shows all the finished scripts

### Methods
- Execute selected scripts: it execute all the scripts you selected (will be added to active automations)
- Clear finished automation: it clears all the finished automations from the finished automations listbox
- terminate selected thread: terminate an active automation (will be added to finished automation)

### Notes
- All the automations are executed as thread, you can activate multiple at once (but keep track of their activation status and activation hotkeys!)
- Active automations usually stores reusable hotkey activation automations (essentially a more complex custom hotkey)
