# Editing tutorial
A detailed description of how to edit
(I use the word "block/blocks" to mean a/multiple command/commands or action/actions)

## Workspace frame

### Description
Workspace allows you to access all of your recorded. You are able to: change the sequence of your automation, record/delete/merge your blocks. You can add multiple workspaces and work with multiple record files. (limited to four workspaces.)

### Buttons
- Add another workspace: all the blocks you selected will be copied to the new workspace.
- Delete main automation: delete main automation or the current listbox
- Merge to main: replace all blocks in main automation to the current workspace
- Concatenate to main: : add all blocks in the current workspace to main automation
- Record a new block: record a new block (same hotkey as the normal record)
- Display new block: display the newly recorded block's information
- Add new block to main: add the newly recorded block in the end of your main automation
- Delete selected block: delete all selected blocks
- Merge selected blocks: combine all your selected blocks to one block and add to the end of the current workspace
- Auto merge blocks: 
  - Press&Release mouse in a short time -> mouse click
  - Two mouse clicks in a short time -> double click
  - Press&Release key in a short time -> keyinput
- Change listbox style (single, multiple, extend)
  - single: you are only able to select one item at once
  - multiple: you can click select multiple items
  - extend: drag to select multiple items

### Listbox actions
- Press "w" to make a/multiple selected blocks go up
- Press "d" to make a/multiple selected blocks go down
- Press "enter" to display the block information and code

## Display information frame

### Description
Display information screen shows the relevant information of the block you selected, include:
- Block type
- Block name
- X-position (not included for keyboard actions)
- Y-position (not included for keyboard actions)
- Action state
- Action type
- Image name
- Waiting time
- Screenshot ( "No image recorded for this block" will be displayed if no image is available )

### method
- Save block data: save your changes on the block information 
- Restore default block value: restore the value (update whenever you save)
- Up a command (merged blocks only): Access the next sub-block or sub-command in your merged block
- Down a command (merged blocks only): Access the previous sub-block or sub-command in your merged block

### Note
Changing values other than block name is not recommended because it will not update your code, you are free to change them but they will not make an impact on the actual performance. 

## Logic frame

### Description
Display the underlying code of your command, you can edit the source code directly from here.

### method
- Save code: save your changes
- Restore default code: restore the code (update whenever you save)
- Add repeat: 
  - Enter the number you want your actions to repeat, and hit "enter" to apply, don't forget to save in the end

### Note
- The code you change will not impact data under the display information as those are mostly a visualization
